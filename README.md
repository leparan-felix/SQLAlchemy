# Object Relations Code Challenge - Articles

## Overview

This project models the relationships between **Authors**, **Magazines**, and **Articles** using **Python** and **SQL**. It captures:

- An `Author` can write many `Articles`
- A `Magazine` can publish many `Articles`
- An `Article` belongs to one `Author` and one `Magazine`
- The `Author`-`Magazine` relationship is many-to-many via `Articles`

---

## Setup Instructions

### Option 1: Using Pipenv
```bash
pipenv install
pipenv shell
