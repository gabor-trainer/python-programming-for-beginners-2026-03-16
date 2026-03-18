from pathlib import Path
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Movie Browser", layout="wide")


@st.cache_data
def load_movies() -> pd.DataFrame:
    csv_path = Path(__file__).parent / "datafiles" / "movies.csv"
    df = pd.read_csv(csv_path)
    df = df.sort_values("title", ignore_index=True)
    return df


def get_all_genres(df: pd.DataFrame) -> list[str]:
    genres = set()
    for entry in df["genres"].dropna():
        for g in entry.split("|"):
            genres.add(g.strip())
    return sorted(genres)


def main():
    st.title("Movie Browser")

    movies = load_movies()
    all_genres = get_all_genres(movies)

    # --- Sidebar controls ---
    selected_genres = st.multiselect("Filter by genre", options=all_genres)
    rows_per_page = int(st.selectbox("Rows per page", options=[10, 50, 100]))

    # --- Filter ---
    if selected_genres:
        mask = movies["genres"].apply(
            lambda g: any(s in g.split("|") for s in selected_genres)
        )
        filtered = movies[mask].reset_index(drop=True)
    else:
        filtered = movies

    total = len(filtered)
    total_pages = max(1, -(-total // rows_per_page))  # ceil division

    # --- Page state (reset on filter/page-size change) ---
    filter_key = (tuple(selected_genres), rows_per_page)
    if "prev_filter_key" not in st.session_state or st.session_state.prev_filter_key != filter_key:
        st.session_state.page = 1
        st.session_state.prev_filter_key = filter_key

    page = st.session_state.page

    # --- Pagination controls ---
    col1, col2, col3, col4, col5 = st.columns([1, 1, 2, 1, 1])
    with col1:
        if st.button("First", disabled=(page <= 1)):
            st.session_state.page = 1
            st.rerun()
    with col2:
        if st.button("Previous", disabled=(page <= 1)):
            st.session_state.page -= 1
            st.rerun()
    with col4:
        if st.button("Next", disabled=(page >= total_pages)):
            st.session_state.page += 1
            st.rerun()
    with col5:
        if st.button("Last", disabled=(page >= total_pages)):
            st.session_state.page = total_pages
            st.rerun()
    with col3:
        start_row = (page - 1) * rows_per_page
        end_row = min(start_row + rows_per_page, total)
        st.markdown(
            f"**Showing {end_row - start_row} of {total} movies (page {page} of {total_pages})**")

    # --- Results table ---
    page_slice = filtered.iloc[start_row:end_row][[
        "movieId", "title", "genres"]]
    st.dataframe(page_slice, use_container_width=True, hide_index=True)


if __name__ == "__main__":
    main()
