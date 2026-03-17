
### **Technical Specification: WordCount CLI**

#### **1. General Overview**
The program is a command-line utility that accepts a string as an argument, performs text analysis, and outputs a formatted statistical report.

#### **2. Dependencies**
*   **Language:** Python 3.x
*   **Library (External):** `tabulate` (for table formatting).
*   **Library (Standard):** `argparse` (CLI parsing), `re` (regex for cleaning), `collections` (counting).

#### **3. Input & Command Line Interface**
*   **Mechanism:** `argparse` will handle the interface.
*   **Usage:** `python wordcount.py "Your input text goes here"`
*   **Argument:** A single positional argument (string) containing the file name of the text to be analyzed. Could be relative or absolute path.

#### **4. Data Processing Pipeline**
The input string will undergo the following transformations in order:
1.  **Line Calculation:** Calculate "Total Lines" by counting newline characters (`\n`) in the raw input.
2.  **Whitespace Normalization:** Convert all sequences of multiple whitespaces (tabs, multiple spaces, newlines) into a single space.
3.  **Character Calculation:** Count the total length of the string *after* whitespace normalization.
4.  **Case Normalization:** Convert the entire string to lowercase.
5.  **Punctuation Removal:** Strip all punctuation marks (e.g., `. , ! ? ; :`) to ensure words like "Apple," and "apple" are treated as the same token.
6.  **Tokenization:** Split the cleaned string into a list of individual words.
7.  **Stop Word Filtering:** Remove words that exist in the "Starter List" (see Section 5).
8.  **Frequency Analysis:** 
    *   Calculate the **Unique Word Count** (the size of the set of filtered words).
    *   Identify the **Top 10** most frequent words from the filtered list.

#### **5. Starter Stop Words List**
The following words will be excluded from the "Top 10" and "Unique Word Count" metrics:
> *a, an, the, and, or, but, if, because, as, until, while, of, at, by, for, with, about, against, between, into, through, during, before, after, above, below, to, from, up, down, in, out, on, off, over, under, again, further, then, once, here, there, when, where, why, how, all, any, both, each, few, more, most, other, some, such, no, nor, not, only, own, same, so, than, too, very, can, will, just, should, now.*

#### **6. Output Specification**
The results will be printed to `stdout` using two distinct tables formatted by `tabulate` (using the `grid` or `fancy_grid` style):

**Table A: General Statistics**
*   **Total Words:** (Count of all words before stop-word filtering).
*   **Total Lines:** (Based on raw input).
*   **Total Characters:** (Based on whitespace-normalized text).
*   **Unique Words:** (Count of distinct words after filtering stop words).

**Table B: Frequency Analysis**
*   A list of the **Top 10** most common words (excluding stop words) and their respective counts.

---

### **Review Checklist**
1.  **Stop Words:** Does the list look sufficient?
2.  **Character Count:** Confirmed that it will be calculated *after* collapsing multiple spaces into one.
3.  **Total Words:** Confirmed this counts *all* words (including stop words) but excludes punctuation.
4.  **Tables:** Is the two-table approach (General Stats + Top 10) acceptable?

**Should I proceed with the code based on this specification?**
