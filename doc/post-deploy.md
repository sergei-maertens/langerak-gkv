# Post deploy notes

## 2025-01-19

**CMS tree fixing**

Make sure to delete orphaned plugins:

```bash
src/manage.py cms delete-orphaned-plugins
```

**Set default church**

Check new checkbox field.
