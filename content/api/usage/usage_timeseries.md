---
title: Get hourly usage for custom metrics
type: apicontent
order: 22.2
external_redirect: /api/#get-hourly-usage-for-custom-metrics
---

## Get hourly usage for custom metrics

Get Hourly Usage For [Custom Metrics](/getting_started/custom_metrics/).

##### Arguments
* **`start_hr`** [*required*]:  
    datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage beginning at this hour
* **`end_hr`** [*optional*, *default*=**1d+start_hr**]:  
    datetime in ISO-8601 format, UTC, precise to hour: [YYYY-MM-DDThh] for usage ending BEFORE this hour
