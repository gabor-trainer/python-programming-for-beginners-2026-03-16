**Data**
- Load `movies.csv` from the same directory as the app
- Parse `genres` column by splitting on `|`
- Sort all movies by `title` A–Z before any filtering or paging

**UI Components**
- A **multiselect dropdown** listing all unique genres (sorted A–Z)
- A **row count selector** — radio or selectbox with options: `10`, `50`, `100`
- A **results table** showing filtered movies (`movieId`, `title`, `genres`)
- A **result count** label e.g. *"Showing 10 of 42 movies (page 1 of 5)"*
- **Pagination controls** — Previous / Next buttons, current page indicator

**Filter & Paging Logic**
- Default state: all movies shown, no genre selected, 10 rows per page, page 1
- Genre filter: show movies containing **any** selected genre (OR logic)
- Changing genre selection resets to **page 1**
- Changing rows-per-page resets to **page 1**
- Previous button disabled on page 1; Next button disabled on last page
- Page slice applied **after** filtering and sorting

**Project Structure**
```
project/
├── pyproject.toml
├── movies.csv
└── app.py
```

**Dependencies (via uv)**
- `streamlit`
- `pandas`

---

Ready to generate the code?