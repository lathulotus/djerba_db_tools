import marimo

__generated_with = "0.21.1"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import marimo as mo
    import pandas as pd
    import numpy as np
    import io
    import re
    import matplotlib.pyplot as plt
    import datetime as dt
    mo.md(" # CouchDB Notebook")
    return io, mo, np, pd, plt, re


@app.cell
def _(mo):
    summary_upload = mo.ui.file(label="Upload one or more summary CSVs", multiple=True)

    mo.hstack([("Summary table generated through the couchDB query pipeline: "), summary_upload]).style(width="fit-content")
    return (summary_upload,)


@app.cell
def _(io, pd, summary_upload):
    if summary_upload.value:
        file_bytes = summary_upload.contents(0)
        summary = pd.read_csv(io.BytesIO(file_bytes))
    else:
        print("Upload valid summary CSV")
    return (summary,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Weekly Summary
    """)
    return


@app.cell
def _(mo, pd, summary):
    summary_weekly = summary.copy()
    summary_weekly["date_reported"] = pd.to_datetime(summary_weekly["date_reported"], errors="coerce")
    summary_weekly = summary_weekly.dropna(subset=["date_reported"])

    # Latest week
    summary_weekly["week_start"] = summary_weekly["date_reported"].dt.to_period("W").apply(lambda r: r.start_time)
    week_latest = summary_weekly["week_start"].max()

    # Custom week
    week_custom_start = mo.ui.date(label="Start date")
    week_custom_end = mo.ui.date(label="End date")

    # Toggle week view
    toggle_weekly = mo.ui.switch(label="Custom date range", value=False)
    return (
        summary_weekly,
        toggle_weekly,
        week_custom_end,
        week_custom_start,
        week_latest,
    )


@app.cell
def _(
    mo,
    pd,
    plt,
    summary_weekly,
    toggle_weekly,
    week_custom_end,
    week_custom_start,
    week_latest,
):
    # Conditional view for custom date
    if toggle_weekly.value:
        weekly_date_controls = mo.vstack([week_custom_start, week_custom_end])
    else:
        weekly_date_controls = mo.md("")

    # Determine week view
    if not toggle_weekly.value:
        selected = summary_weekly[summary_weekly["week_start"] == week_latest]
        last_report_date = selected["date_reported"].max()
        title_date = f"{week_latest.date()} to {last_report_date.date()}"
    else:
        week_start = pd.to_datetime(week_custom_start.value)
        week_end = pd.to_datetime(week_custom_end.value)
        selected = summary_weekly[
            (summary_weekly["date_reported"] >= week_start) &
            (summary_weekly["date_reported"] <= week_end)]
        title_date = f"{week_start.date()} to {week_end.date()}"

    weekly_counts = selected.groupby("project").size().reset_index(name="count")
    total_per_week = int(weekly_counts["count"].sum()) if not weekly_counts.empty else 0
    fig1, ax1 = plt.subplots(figsize=(8,5))

    if weekly_counts.empty:
        ax1.text(0.5, 0.5, "No data in date range", ha="center", va="center")
        ax1.set_xticks([])
        ax1.set_yticks([])
        ymax = 5
    else:
        bars = ax1.bar(weekly_counts["project"], weekly_counts["count"],color="steelblue", edgecolor="white")
        for bar in bars:
            ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height(),
                     str(bar.get_height()), ha="center", va="bottom", fontsize=10)
        ymax = weekly_counts["count"].max()

    ax1.set_ylim(0, ymax * 1.15)
    ax1.set_title(f"Weekly Summary of Completed Reports (From {title_date})")
    ax1.set_xlabel("Project")
    ax1.set_ylabel("Number of Reports")
    ax1.grid(True, alpha=0.6)
    plt.xticks(rotation=45)
    plt.tight_layout()

    weekly_control_panel = mo.vstack([
        toggle_weekly,
        weekly_date_controls,
        mo.md("---"),
        mo.md(f"**Total reports:** {total_per_week}")
    ]).style(width="30%")

    mo.hstack([
        weekly_control_panel,
        mo.vstack([mo.carousel([fig1])]).style(width="70%")]).style(width="100%")
    return


@app.cell
def _(mo):
    mo.md("""
    ---
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Summary Table
    """)
    return


@app.cell
def _(mo, summary):
    # Preset column filters
    presets = {
        "HRD": ["report_id", "donor", "project", "failed", "coverage", "hrd_status", "hrd_value"]
    }
    preset_view = mo.ui.dropdown(
        options = ["None"] + list(presets.keys()),
        value = "None",
        label = "Prefiltered view of summary table:"
    )

    # Custom column filters
    column_view = mo.ui.multiselect(
        options = list(summary.columns),
        value = list(summary.columns),
        label = "Custom view of summary table:"
    )

    mo.hstack([preset_view, mo.md(" **|** "), column_view]).style(width="60%")
    return column_view, preset_view, presets


@app.cell
def _(column_view, mo, pd, preset_view, presets, summary):
    if preset_view.value != "None":
        visible_columns = [c for c in presets[preset_view.value] if c in summary.columns]
    else:
        visible_columns = column_view.value

    summary_table = summary[visible_columns].copy()
    if "date_reported" in summary_table.columns:
        summary_table["date_reported"] = pd.to_datetime(summary_table["date_reported"], errors="coerce").dt.strftime("%Y-%m-%d")
    mo.ui.table(summary_table)
    return


@app.cell
def _(mo):
    mo.md("""
    ---
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Summary Figures
    """)
    return


@app.cell
def _(mo, summary):
    # Select quantitative histograms
    quanthist_select = mo.ui.multiselect(
        options=list(summary.select_dtypes(include=["number"]).columns),
        value=[],
        label="Generate histograms for:"
    )

    # Select qualitative histograms
    qual_exclude = ["report_id", "purple_zip", "sequenza_solution"]
    qualhist_select = mo.ui.multiselect(
        options=[c for c in summary.select_dtypes(include=["string"]).columns if c not in qual_exclude],
        value=[],
        label="Generate bar plots for:"
    )
    return qualhist_select, quanthist_select


@app.cell
def _(mo, quanthist_select, summary):
    # Controls for bar plots
    top_n_view = mo.ui.number(label="Top ", value=20)

    # Controls for histograms
    x_min_input = {}
    x_max_input = {}
    x_axis_content = []
    for c in quanthist_select.value:
        col_series = summary[c].dropna()
        col_min = col_series.min()
        col_max = col_series.max()
    
        x_min_input[c] = mo.ui.number(label=f"Min", value=None)
        x_max_input[c] = mo.ui.number(label=f"Max", value=None)
    
        x_axis_content.append(
            mo.vstack([
                mo.md(f"**{c}**"),
                mo.hstack([
                    x_min_input[c].style(width="120px"),
                    x_max_input[c].style(width="120px")])
            ])
        )
    
    bin_select = mo.ui.slider(start=0, stop=100, value=10, label="Number of bins: ")
    date_start = mo.ui.date(label="From", value="2020-01-01")
    date_end = mo.ui.date(label="To")

    apply_button = mo.ui.button(label="Apply")
    return (
        apply_button,
        bin_select,
        date_end,
        date_start,
        top_n_view,
        x_axis_content,
        x_max_input,
        x_min_input,
    )


@app.cell
def _(
    apply_button,
    bin_select,
    date_end,
    date_start,
    mo,
    np,
    pd,
    plt,
    qualhist_select,
    quanthist_select,
    re,
    summary,
    top_n_view,
    x_axis_content,
    x_max_input,
    x_min_input,
):
    apply_button.value

    # Date select
    start_date = pd.to_datetime(date_start.value)
    end_date = pd.to_datetime(date_end.value)
    summary["date_reported"] = pd.to_datetime(summary["date_reported"], errors="coerce")
    filtered_summary = summary[
        (summary["date_reported"] >= start_date) &
        (summary["date_reported"] <= end_date)
    ]
    if filtered_summary.empty:
        plots = [mo.md("No data in date range")]
    else:
        plots = []

    # Add metrics
    metrics = {"TMB": "(Mb)", "PGA": "(%)"}

    # Plot styling
    plt.style.use("ggplot")
    plt.rcParams["axes.facecolor"] = "white"
    plt.rcParams["figure.facecolor"] = "white"
    plt.rcParams["axes.grid"] = True
    plt.rcParams["grid.color"] = "lightgrey"

    # Quantitative plots
    for col in quanthist_select.value:
        series = filtered_summary[col].dropna()

        label = col.replace("_", " ").title()
        label = re.sub(r"\bSnv\b", "SNV", label)
        label = re.sub(r"\bCnv\b", "CNV", label)
        label = re.sub(r"\bPga\b", "PGA", label)
        label = re.sub(r"\bHrd\b", "HRD", label)
        label = re.sub(r"\bMsi\b", "MSI", label)
        label = re.sub(r"\bTmb\b", "TMB", label)

        suffix = ""
        for key, val in metrics.items():
            if key in col.upper():
                suffix = f" {val}"
                break

        xmin = x_min_input[col].value
        xmax = x_max_input[col].value
        xmin = float(xmin) if xmin is not None else None
        xmax = float(xmax) if xmax is not None else None

        plot_series = series.copy()
        if xmin is not None:
            plot_series = plot_series[plot_series >= xmin]
        if xmax is not None:
            plot_series = plot_series[plot_series <= xmax]

        fig2, ax2 = plt.subplots()
        if plot_series.empty:
            quant_x_min = series.min()
            quant_x_max = series.max()
        else:
            quant_x_min = plot_series.min()
            quant_x_max = plot_series.max()

        quant_x_min_final = xmin if xmin is not None else quant_x_min
        quant_x_max_final = xmax if xmax is not None else quant_x_max

        edges = np.linspace(quant_x_min_final, quant_x_max_final, bin_select.value + 1)
        ax2.hist(plot_series, bins=edges, color="steelblue", edgecolor="white")
        ax2.set_xlim(quant_x_min_final, quant_x_max_final)
        ax2.set_xticks(edges)
        plt.xticks(rotation=45, ha="right")
        ax2.set_title(f"Histogram of {label}")
        ax2.set_xlabel(label + suffix)
        ax2.set_ylabel("Case Count")
        ax2.set_ylim(0, ax2.get_ylim()[1] * 1.1)

        plots.append(fig2)

    # Qualitative plots
    for col in qualhist_select.value:
        series = filtered_summary[col].dropna()
    
        label = col.replace("_", " ").title()
        label = re.sub(r"\bSnv\b", "SNV", label)
        label = re.sub(r"\bCnv\b", "CNV", label)
        label = re.sub(r"\bPga\b", "PGA", label)
        label = re.sub(r"\bHrd\b", "HRD", label)
        label = re.sub(r"\bMsi\b", "MSI", label)
        label = re.sub(r"\bTmb\b", "TMB", label)
    
        qualexpand = []
        for cell in series:
            for item in cell.split(","):
                item_norm = item.strip()
                if item_norm:
                    qualexpand.append(item_norm)
        counts = pd.Series(qualexpand).value_counts()
        top_n = top_n_view.value if top_n_view.value is not None else 20
        counts = counts.head(int(top_n))

        fig3, ax3 = plt.subplots()
        ax3.bar(counts.index.astype(str), counts.values, color="steelblue", edgecolor="white")

        ymax3 = counts.max()
        ax3.set_ylim(0, ymax3 * 1.15)

        ax3.set_title(f"Counts of {label}")
        ax3.set_xlabel(label)
        ax3.set_ylabel("Counts")
        plt.xticks(rotation=45, ha="right")

        plots.append(fig3)

    # View settings and plot
    left_panel = mo.vstack([
        mo.md("### Bar Plot Settings"),
        qualhist_select,
        top_n_view.style(width="15px"),
        mo.md("---"),
        mo.md("### Histogram Settings"),
        quanthist_select,
        bin_select,
        mo.md("### X-axis Limits").style(margin_top="15px"),
        *x_axis_content,
        apply_button,
        mo.md("---"),
        mo.md("### All Settings"),
        mo.hstack([date_start, date_end])]).style(width="30%", padding="15px")

    right_panel = mo.vstack([
        mo.carousel(plots)
    ]).style(width="70%", padding="15px")

    mo.hstack([left_panel, right_panel])
    return


if __name__ == "__main__":
    app.run()
