# LakePulse Data Quality Strategy

## Validation Rules

The Silver layer enforces:

- Non-null ride IDs
- Non-null driver IDs
- Non-null rider IDs
- Valid timestamps
- Deduplication by ride_id

# Late Arriving Data

The pipeline uses:
- event-time watermarking
- 10-minute lateness threshold

Late events beyond the threshold are dropped.

# Future Enhancements

Planned improvements:
- schema registry integration
- quarantine buckets
- anomaly detection
- automated quality scoring