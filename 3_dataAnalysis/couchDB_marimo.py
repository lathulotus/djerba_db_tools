import marimo

__generated_with = "0.21.1"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import marimo as mo
    import pandas as pd
    import numpy as np
    import io, re, datetime as dt
    import matplotlib.pyplot as plt
    from matplotlib.ticker import MaxNLocator
    mo.md(" # CouchDB Analytics")
    return MaxNLocator, io, mo, np, pd, plt, re


@app.cell
def _(mo):
    summary_upload = mo.ui.file(label="Upload CSV", multiple=True)
    mo.hstack([("Summary CSV from query pipeline: "), summary_upload]).style(width="fit-content")
    return (summary_upload,)


@app.cell
def _(io, pd, summary_upload):
    if summary_upload.value:
        summary = pd.read_csv(io.BytesIO(summary_upload.contents(0)))
    else:
        print("Upload summary CSV")
    return (summary,)


@app.cell
def _(mo):
    mo.vstack([mo.md("---"), mo.md("## Weekly Summary").style(padding_top="5px")])
    return


@app.cell
def _(mo, pd, summary):
    # Create UI elements for weekly summary plot
    summary_weekly = summary.copy()
    summary_weekly["date_reported"] = pd.to_datetime(summary_weekly["date_reported"], errors="coerce")
    summary_weekly = summary_weekly.dropna(subset=["date_reported"])
    summary_weekly["week_start"] = summary_weekly["date_reported"].dt.to_period("W").apply(lambda r: r.start_time)

    week_custom_start = mo.ui.date(label="Start date")
    week_custom_end = mo.ui.date(label="End date")
    toggle_weekly = mo.ui.switch(label="Custom date range", value=False)
    return summary_weekly, toggle_weekly, week_custom_end, week_custom_start


@app.cell
def _(
    mo,
    pd,
    plt,
    summary_weekly,
    toggle_weekly,
    week_custom_end,
    week_custom_start,
):
    # Plot weekly summary
    weekly_date_controls = mo.vstack([week_custom_start, week_custom_end]) if toggle_weekly.value else mo.md("")

    if not toggle_weekly.value:
        week_start = summary_weekly["week_start"].max()
        selected = summary_weekly[summary_weekly["week_start"] == week_start]
        week_end = selected["date_reported"].max()
    else:
        week_start = pd.to_datetime(week_custom_start.value)
        week_end = pd.to_datetime(week_custom_end.value)
        selected = summary_weekly[(summary_weekly["date_reported"] >= week_start) & (summary_weekly["date_reported"] <= week_end)]

    weekly_counts = selected.groupby("project").size().reset_index(name="count")
    total_per_week = int(weekly_counts["count"].sum()) if not weekly_counts.empty else 0

    fig_weekly, ax_weekly = plt.subplots(figsize=(8,5))
    if weekly_counts.empty:
        ax_weekly.text(0.5, 0.5, "No data in date range", ha="center", va="center")
        ax_weekly.set_xticks([]); ax_weekly.set_yticks([]); ymax = 5
    else:
        bars_weekly = ax_weekly.bar(weekly_counts["project"], weekly_counts["count"],color="#7cb066ff", edgecolor="white")
        for bar_w in bars_weekly:
            ax_weekly.text(bar_w.get_x() + bar_w.get_width()/2, bar_w.get_height(),
                           str(bar_w.get_height()), ha="center", va="bottom", fontsize=10)
        ymax = weekly_counts["count"].max()

    ax_weekly.set_ylim(0, ymax * 1.15)
    ax_weekly.set_title(f"Summary of Completed Reports ({week_start.date()} to {week_end.date()})")
    ax_weekly.set_xlabel("Project")
    ax_weekly.set_ylabel("Number of Reports")
    ax_weekly.grid(True, linestyle=":", alpha=0.3)
    ax_weekly.spines["left"].set_visible(True); ax_weekly.spines["left"].set_color("black"); ax_weekly.spines["left"].set_linewidth(0.5)
    ax_weekly.spines["bottom"].set_visible(True); ax_weekly.spines["bottom"].set_color("black"); ax_weekly.spines["bottom"].set_linewidth(0.5)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    mo.hstack([
        mo.vstack([toggle_weekly, weekly_date_controls,
                   mo.md("---"),
                   mo.md(f"**Total reports:** {total_per_week}")]).style(width="25%"),
        mo.vstack([mo.carousel([fig_weekly])]).style(width="75%")]).style(width="100%")
    return


@app.cell
def _(mo):
    mo.vstack([mo.md("---"), mo.md("## Summary Table").style(padding_top="5px")])
    return


@app.cell
def _(mo, summary):
    # Create UI elements for summary table
    column_view = mo.ui.multiselect(options = (list(summary.columns)),
                                    value = list(summary.columns),
                                    label = "Custom view of summary table: ")
    return (column_view,)


@app.cell
def _(column_view, mo, pd, summary):
    # View summary table
    summary_table = summary[column_view.value].copy()
    if "date_reported" in summary_table.columns:
        summary_table["date_reported"] = pd.to_datetime(summary_table["date_reported"], errors="coerce").dt.strftime("%Y-%m-%d")

    mo.vstack([column_view.style(padding_bottom="10px"), mo.ui.table(summary_table)])
    return


@app.cell
def _(mo):
    mo.vstack([mo.md("---"), mo.md("## Descriptive Analytics").style(padding_top="5px")])
    return


@app.cell
def _(mo, summary):
    # Create UI elements for plot selection (numeric & categorical)
    num_hist = mo.ui.multiselect(
        options=sorted(list(summary.select_dtypes(include=["number"]).columns)),
        value=[],
        label="Generate histograms for:")

    cat_select = mo.ui.multiselect(
        options=sorted([c for c in summary.select_dtypes(include=["string"]).columns]),
        value=[],
        label="Generate bar plots for:")
    return cat_select, num_hist


@app.cell
def _(mo, normalize_name, num_hist):
    # Controls for plots
    cat_top_n = mo.ui.number(label="Top ", value=20)

    x_min_input, x_max_input, x_axis_content = {}, {}, []
    for num_hist_col in num_hist.value:
        x_min_input[num_hist_col] = mo.ui.number(label=f"Min", value=None)
        x_max_input[num_hist_col] = mo.ui.number(label=f"Max", value=None)
        x_axis_content.append(mo.vstack([mo.md(f"####{normalize_name(num_hist_col)}"),
                                         mo.hstack([x_min_input[num_hist_col],
                                                    x_max_input[num_hist_col]]).style(width="fit-content")]))

    bin_select = mo.ui.slider(start=0, stop=100, value=10, label="Number of bins: ")
    date_start_select = mo.ui.date(label="From", value="2022-01-01")
    date_end_select = mo.ui.date(label="To")
    apply_button = mo.ui.button(label="Apply")
    return (
        apply_button,
        bin_select,
        cat_top_n,
        date_end_select,
        date_start_select,
        x_axis_content,
        x_max_input,
        x_min_input,
    )


@app.cell
def _(
    apply_button,
    bin_select,
    cat_select,
    cat_top_n,
    date_end_select,
    date_start_select,
    italicize_genes,
    mo,
    normalize_name,
    np,
    num_hist,
    pd,
    plt,
    summary,
    x_axis_content,
    x_max_input,
    x_min_input,
):
    apply_button.value

    # Date select
    summary["date_reported"] = pd.to_datetime(summary["date_reported"], errors="coerce")
    filtered_summary = summary[(summary["date_reported"] >= pd.to_datetime(date_start_select.value)) &
                               (summary["date_reported"] <= pd.to_datetime(date_end_select.value))]
    plots_desc = [] if not filtered_summary.empty else [mo.md("No data in date range")]

    # Quantitative plots
    metrics = {"TMB": "(Mb)", "PGA": "(%)"}
    for num_col in num_hist.value:
        series = filtered_summary[num_col].dropna()
        label = normalize_name(num_col)
        suffix = next((f" {val}" for key, val in metrics.items() if key in num_col.upper()), "")

        xmin = x_min_input[num_col].value
        xmax = x_max_input[num_col].value
        xmin = float(xmin) if xmin is not None else None
        xmax = float(xmax) if xmax is not None else None

        plot_series = series.copy()
        if xmin is not None:
            plot_series = plot_series[plot_series >= xmin]
        if xmax is not None:
            plot_series = plot_series[plot_series <= xmax]

        quant_x_min = series.min() if plot_series.empty else plot_series.min()
        quant_x_max = series.max() if plot_series.empty else plot_series.max()
        quant_x_min_final = xmin if xmin is not None else quant_x_min
        quant_x_max_final = xmax if xmax is not None else quant_x_max

        fig_hist_num, ax_hist = plt.subplots()
        edges = np.linspace(quant_x_min_final, quant_x_max_final, bin_select.value + 1)
        ax_hist.hist(plot_series, bins=edges, color="#7cb066ff", edgecolor="white")
        ax_hist.set_xlim(quant_x_min_final, quant_x_max_final)
        ax_hist.set_xticks(edges)
        plt.xticks(rotation=45, ha="right")
        ax_hist.set_axisbelow(True)
        ax_hist.grid(True, linestyle=":", alpha=0.3)
        ax_hist.set_title(f"Histogram of {label}")
        ax_hist.set_xlabel(label + suffix)
        ax_hist.set_ylabel("Case Count")
        ax_hist.set_ylim(0, ax_hist.get_ylim()[1] * 1.1)
        ax_hist.spines["left"].set_visible(True); ax_hist.spines["left"].set_color("black"); ax_hist.spines["left"].set_linewidth(0.5)
        ax_hist.spines["bottom"].set_visible(True); ax_hist.spines["bottom"].set_color("black"); ax_hist.spines["bottom"].set_linewidth(0.5)
        plots_desc.append(fig_hist_num)

    # Qualitative plots
    for cat_col in cat_select.value:
        series = filtered_summary[cat_col].dropna()
        label = normalize_name(cat_col)

        qualexpand = []
        for cell in series:
            for item in cell.split(","):
                item_norm = item.strip()
                if item_norm:
                    qualexpand.append(item_norm)

        counts = pd.Series(qualexpand).value_counts()
        counts = counts.head(cat_top_n.value or 20)

        fig_bar, ax_bar = plt.subplots()
        ax_bar.bar(counts.index.astype(str), counts.values, color="#7cb066ff", edgecolor="white")
        ymax_bar = counts.max()
        ax_bar.set_ylim(0, ymax_bar * 1.15)
        ax_bar.set_title(f"Counts of {label}")
        ax_bar.set_xlabel(label)
        ax_bar.set_ylabel("Counts")
        if cat_col in ("snv_genes", "cnv_genes", "fusion_pairs"):
            styled = [italicize_genes(gene_label) for gene_label in counts.index.astype(str)]
            ax_bar.set_xticks(range(len(styled)))
            ax_bar.set_xticklabels(styled, rotation=45, ha="right")
        else:
            plt.xticks(rotation=45, ha="right")
        ax_bar.set_axisbelow(True)
        ax_bar.grid(True, linestyle=":", alpha=0.3)
        ax_bar.spines["left"].set_visible(True); ax_bar.spines["left"].set_color("black"); ax_bar.spines["left"].set_linewidth(0.5)
        ax_bar.spines["bottom"].set_visible(True); ax_bar.spines["bottom"].set_color("black"); ax_bar.spines["bottom"].set_linewidth(0.5)
        plots_desc.append(fig_bar)

    # View settings & plot
    left_panel = mo.vstack([
        mo.md("### Bar Plot Settings"), cat_select, cat_top_n.style(width="15px"),
        mo.md("---\n ### Histogram Settings"), num_hist, bin_select,
        mo.md("### X-axis Limits").style(margin_top="15px"), *x_axis_content, apply_button,
        mo.md("---\n ### All Settings"), mo.hstack([date_start_select, date_end_select])]).style(width="30%", padding="15px")
    right_panel = mo.vstack([
        mo.carousel(plots_desc)]).style(width="70%", padding="10px")
    mo.hstack([left_panel, right_panel])
    return


@app.cell
def _(mo):
    mo.vstack([mo.md("---"), mo.md("## Cumulative Case Trends").style(padding_top="5px")])
    return


@app.cell
def _(mo, summary):
    # Cohort: select general cohort
    cohort_select = mo.ui.dropdown(
        label = "Cohort: ",
        options = sorted([c for c in summary.select_dtypes(include=["string"]).columns]),
        value="hrd_status")
    return (cohort_select,)


@app.cell
def _(cohort_select, mo, summary):
    # Cohort: filter specific cohorts
    cohort_filter = mo.ui.multiselect(
        label = "Filter: ",
        options = sorted(summary[cohort_select.value].dropna().unique()) if cohort_select.value else [],
        value=["HRD"])
    return (cohort_filter,)


@app.cell
def _(mo, summary):
    # Group: select general group
    group_select = mo.ui.dropdown(
        label = "Group: ",
        options = sorted([c for c in summary.columns]),
        value = "coverage")
    return (group_select,)


@app.cell
def _(group_select, mo, summary):
    # Group: user input depends on group type (string vs integer)
    if group_select.value:
        if summary[group_select.value].dtype.kind in "iuf":
            group_input = mo.ui.text(
                label = "Filter: ",
                placeholder = ">=115, <115, ==115",
                value=">=115, <115")
        else:
            group_input = mo.ui.multiselect(
                label = "Filter: ",
                options = sorted(summary[group_select.value].dropna().unique()))
    else:
        group_input= mo.md("")
    return (group_input,)


@app.cell
def _(group_input, group_select, summary):
    # Group: filter specific groups
    group_filters = []
    if group_select.value and group_input is not None:    
        if summary[group_select.value].dtype.kind in "iuf":
            group_input_raw = group_input.value.strip()
            if group_input_raw:
                group_input_expr = [e.strip() for e in group_input_raw.split(",") if e.strip()]
                for group_expr_temp in group_input_expr:
                    group_filters.append({
                        "column": group_select.value,
                        "type": "numeric",
                        "input": group_expr_temp})
        else:
            group_input_raw = group_input.value
            if group_input_raw:
                group_filters.append({
                    "column": group_select.value,
                    "type": "categorical",
                    "input": list(group_input_raw)})
    return (group_filters,)


@app.cell
def _(mo, summary):
    # Colour: select colour bar
    colour_bar = mo.ui.dropdown(
        label = "Colour by: ",
        options = sorted([c for c in summary.select_dtypes(include=["number"]).columns]),
        value="coverage")

    # Date: select date range
    date_cols = [c for c in summary.columns if "date_reported" in c.lower()]
    date_start_cumulative = mo.ui.date(label = "From: ", value = "2024-01-01")
    date_end_cumulative = mo.ui.date(label = "To: ")

    # Percent line
    percent_line_cc = mo.ui.checkbox(label="Percent Line")
    return (
        colour_bar,
        date_end_cumulative,
        date_start_cumulative,
        percent_line_cc,
    )


@app.cell
def _(group_filters, group_select, mo, percent_line_cc, summary):
    # Percent line: UI
    if percent_line_cc.value:
        if group_select.value:
            dtype = summary[group_select.value].dtype

            if dtype.kind in "iuf":
                options_percent = []
                for gf_temp in group_filters:
                    if gf_temp["column"] == group_select.value:
                        options_percent.append((gf_temp["column"], gf_temp["input"]))
                percent_interval_cc = mo.ui.dropdown(
                    options=["Daily", "Weekly", "Monthly", "Quarterly", "Yearly"],
                    label="Interval: ",
                    value="Monthly")
                percent_focus_cc = mo.ui.dropdown(
                    label="Focus on:",
                    options=options_percent)
            else:
                unique_vals = sorted(summary[group_select.value].dropna().unique().tolist())
                percent_interval_cc = mo.ui.dropdown(
                    options=["Daily", "Weekly", "Monthly", "Quarterly", "Yearly"],
                    label="Interval: ",
                    value="Monthly")
                percent_focus_cc = mo.ui.dropdown(
                    label="Focus on:",
                    options=[(group_select.value, v) for v in unique_vals])
        else:
            percent_interval_cc = mo.md("")
            percent_focus_cc = mo.md("")
    else:
        percent_interval_cc = mo.md("")
        percent_focus_cc = mo.md("")

    percent_interval_controls = (
        percent_interval_cc if percent_line_cc.value else mo.md(""))
    return percent_focus_cc, percent_interval_cc


@app.cell
def _(
    MaxNLocator,
    cohort_filter,
    cohort_select,
    colour_bar,
    date_end_cumulative,
    date_start_cumulative,
    group_filters,
    group_input,
    group_select,
    mo,
    normalize_name,
    pd,
    percent_focus_cc,
    percent_interval_cc,
    percent_line_cc,
    plt,
    summary,
):
    # Putting together plot settings
    df_cc = summary.copy()
    if cohort_select.value and cohort_filter.value:
        df_cc = df_cc[df_cc[cohort_select.value].isin(cohort_filter.value)]

    # Handling groups
    group_lines = []
    for gf in group_filters or []:
        gf_col = gf["column"]
        if gf["type"] == "numeric":
            group_lines.append({"column": gf_col,
                                "value": gf['input'],
                                "label": normalize_name(str(gf['input'])),
                                "expr": f"{gf_col} {gf['input']}"})
        else:
            for gf_val in gf["input"]:
                group_lines.append({"column": gf_col,
                                    "value": gf_val,
                                    "label": normalize_name(str(gf_val)),
                                    "expr": f"{gf_col} == {repr(gf_val)}"})

    # Handling date
    if "date_reported" in df_cc.columns:
        df_cc["date_reported"] = pd.to_datetime(df_cc["date_reported"], errors="coerce")
        df_cc = df_cc[(df_cc["date_reported"] >= pd.to_datetime(date_start_cumulative.value)) &
                      (df_cc["date_reported"] <= pd.to_datetime(date_end_cumulative.value))]

    # Plot cumulative cases
    if df_cc.empty:
        right_panel_cc = mo.md("No data selected")
    else:
        fig_cc, ax_cc = plt.subplots(figsize=(12, 7))
        handles_cc = []
        labels_cc = []

        if not group_lines:
            group_lines = [{"column": None, "value": None, "label": "All cases", "expr": None}]

        colour_by = colour_bar.value or None
        if colour_by:
            col_all = []
            for gl in group_lines if group_lines else [{"expr": None}]:
                sub_cc = df_cc.query(gl["expr"]) if gl["expr"] else df_cc
                if not sub_cc.empty:
                    col_all.extend((sub_cc.groupby("date_reported")[colour_by].mean().dropna().tolist()))
            if col_all:
                col_bar_min, col_bar_max = min(col_all), max(col_all)
            else:
                colour_by = None

        markers = ["o", "s", "^", "D", "P", "X", ]
        for mt, gl in enumerate(group_lines):
            marker_type = markers[mt % len(markers)]
            label_cc = gl["label"]
            sub_cc = df_cc.query(gl["expr"]) if gl["expr"] else df_cc
            if sub_cc.empty:
                continue

            group_cc = sub_cc.groupby("date_reported").size().reset_index(name="Case_Count")
            if colour_by:
                group_cc["Avg_Value"] = sub_cc.groupby("date_reported")[colour_by].mean().values
            group_cc["Cumulative_Count"] = group_cc["Case_Count"].cumsum()

            ax_cc.plot(
                group_cc["date_reported"],
                group_cc["Cumulative_Count"],
                color="steelblue",
                linewidth=2,
                alpha=0.5,)

            if colour_by:
                sc = ax_cc.scatter(
                    group_cc["date_reported"],
                    group_cc["Cumulative_Count"],
                    c=group_cc["Avg_Value"],
                    cmap="viridis",
                    s=60,
                    marker=marker_type,
                    edgecolors="w",
                    vmin=col_bar_min,
                    vmax=col_bar_max,)
                sc.set_label(label_cc)
                handles_cc.append(sc)
                labels_cc.append(label_cc)
            else:
                line_cc, = ax_cc.plot(
                    group_cc["date_reported"],
                    group_cc["Cumulative_Count"],
                    marker=marker_type,
                    linestyle="none",
                    label=label_cc,)
                handles_cc.append(line_cc)
                labels_cc.append(label_cc)

        legend_title_cc = normalize_name(group_lines[0]["column"]) if group_lines else "Groups"
        if (percent_line_cc.value
            and isinstance(percent_focus_cc, mo.ui.dropdown)
            and percent_focus_cc.value
            and "date_reported" in df_cc.columns):

            interval_map = {"daily": lambda s: s,
                            "weekly": lambda s: s.dt.to_period("W").dt.start_time,
                            "monthly": lambda s: s.dt.to_period("M").dt.start_time,
                            "quarterly": lambda s: s.dt.to_period("Q").dt.start_time,
                            "yearly": lambda s: s.dt.to_period("Y").dt.start_time}
            interval_cc = (percent_interval_cc.value or "Daily").lower()
            df_cc["_period"] = interval_map[interval_cc](df_cc["date_reported"])

            if "_period" in df_cc.columns:
                total = df_cc.groupby("_period").size().rename("Total")
                percent_col, percent_val = percent_focus_cc.value           
                focus_sub = (df_cc.query(f"{percent_col} {percent_val}") if summary[percent_col].dtype.kind in "iuf"
                            else df_cc[df_cc[percent_col] == percent_val])
                focus_line = (focus_sub.groupby("_period").size().rename("Focus").reindex(total.index, fill_value=0))

                percent_df = pd.concat([total, focus_line], axis=1)
                percent_df["Percent"] = (percent_df["Focus"] / percent_df["Total"]) * 100

                ax_percent = ax_cc.twinx()
                ax_percent.grid(False); ax_percent.spines["left"].set_visible(False); ax_percent.spines["bottom"].set_visible(False)
                ax_percent.plot(
                    percent_df.index,
                    percent_df["Percent"],
                    color="darkred",
                    linewidth=1.5,
                    label=f"% {normalize_name(str(percent_val))}",)
                ax_percent.set_ylabel(f"Percent of {interval_cc.capitalize()} Cases (%)")
                ax_percent.set_ylim(0, 100)

                lines_cc1, labels_cc1 = ax_cc.get_legend_handles_labels()
                lines_cc2, labels_cc2 = ax_percent.get_legend_handles_labels()
                ax_cc.legend(lines_cc1 + lines_cc2, labels_cc1 + labels_cc2, title=legend_title_cc)

                if colour_by:
                    cbar = fig_cc.colorbar(handles_cc[-1], ax=ax_percent, location="right", pad=0.1)
                    cbar.set_label(colour_by)
                    cbar.locator = MaxNLocator(integer=True)
                    cbar.update_ticks()
                    cbar.outline.set_edgecolor("black")
                    cbar.outline.set_linewidth(0.6)
        else:
            if handles_cc:
                legend_title_cc = normalize_name(group_lines[0]["column"]) if group_lines else "Groups"
                ax_cc.legend(handles_cc, labels_cc, title=legend_title_cc)
                if colour_by:
                    cbar = fig_cc.colorbar(handles_cc[-1], ax=ax_cc)
                    cbar.set_label(colour_by)
                    cbar.locator = MaxNLocator(integer=True)
                    cbar.update_ticks()
                    cbar.outline.set_edgecolor("black")
                    cbar.outline.set_linewidth(0.6)

        ax_cc.set_title("Cumulative Case Accrual Over Time")
        ax_cc.set_xlabel("Date Reported")
        ax_cc.set_xlim(pd.to_datetime(date_start_cumulative.value), pd.to_datetime(date_end_cumulative.value))
        ax_cc.set_ylabel("Number of Cases (Cumulative)")
        ax_cc.grid(True, linestyle=":")
        ax_cc.spines["left"].set_visible(True); ax_cc.spines["left"].set_color("black"); ax_cc.spines["left"].set_linewidth(0.5)
        ax_cc.spines["bottom"].set_visible(True); ax_cc.spines["bottom"].set_color("black"); ax_cc.spines["bottom"].set_linewidth(0.5)
        fig_cc.autofmt_xdate()
        right_panel_cc = mo.carousel([fig_cc]).style(width="75%")

    # View settings and plot
    left_panel_cc = mo.vstack([
        mo.md("### Cohort"), cohort_select, cohort_filter,
        mo.md("---\n ### Groups"), group_select, group_input,
        mo.md("---\n ### Colour Bar"), colour_bar,
        mo.md("---\n ### Date"), date_start_cumulative, date_end_cumulative,
        mo.md("---\n ### Percent Line"), percent_line_cc, percent_focus_cc, percent_interval_cc,]).style(width="25%")
    mo.hstack([left_panel_cc, right_panel_cc])
    return


@app.cell(hide_code=True)
def _(re):
    def normalize_name(text):
        if not text:
            return ""
        text = text.replace("_", " ").title()
        text = re.sub(r"\bSnv\b", "SNV", text)
        text = re.sub(r"\bCnv\b", "CNV", text)
        text = re.sub(r"\bPga\b", "PGA", text)
        text = re.sub(r"\bHrd\b", "HRD", text)
        text = re.sub(r"\bHrp\b", "HRP", text)
        text = re.sub(r"\bMsi\b", "MSI", text)
        text = re.sub(r"\bTmb\b", "TMB", text)
        return text

    def italicize_genes(gene_raw):
        if "::" in gene_raw:
            formatted = []
            for part in gene_raw.split("::"):
                if part.isupper():
                    formatted.append(f"$\\it{{{part}}}$")
                else:
                    formatted.append(part)
            return "::".join(formatted)
        if gene_raw.isupper():
            return f"$\\it{{{gene_raw}}}$"
        return gene_raw

    return italicize_genes, normalize_name


if __name__ == "__main__":
    app.run()
