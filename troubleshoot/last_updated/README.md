## Last Updated
> [Repository](./last_updated) | [Ticket]()

Last updated field saves in date/month/year format along with string timestamp (i.e., 30/01/2026_12:34:10Z). To allow for simple querying, format can be changed to year/month/date, and timestamp can be removed (or saved to another field if required).

**TASK**: Edit `database.py` to change the last_updated field
1. Edit from d/m/y to y-m-d
2. Remove timestamp or save to another field if required