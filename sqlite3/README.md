# SQLite Examples

This directory contains SQLite database examples and demonstrations.

## 📁 Files

- `demo.py` - Python demonstration script
- `favorites.py` - Example working with favorites data
- `favorites.csv` - Sample CSV data
- `favorites.db` - SQLite database file
- `shows.db` - SQLite database with shows data
- `readme.txt` - Additional notes

## 🚀 Quick Start

### Python Example

```bash
python demo.py
# or
python favorites.py
```

### Using SQLite Command Line

```bash
sqlite3 favorites.db
```

Then you can run SQL commands:
```sql
.tables
SELECT * FROM favorites;
```

## 📚 Resources

- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [SQLite Tutorial](https://www.sqlitetutorial.net/)
- [Python sqlite3 Module](https://docs.python.org/3/library/sqlite3.html)

## 💡 Common SQLite Commands

- `.tables` - List all tables
- `.schema` - Show database schema
- `.mode column` - Set column display mode
- `.headers on` - Show column headers
- `.quit` - Exit SQLite

