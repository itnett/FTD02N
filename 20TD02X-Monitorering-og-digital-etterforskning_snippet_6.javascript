// Kibana Visualization
{
  "title": "Syslog Messages",
  "type": "table",
  "params": {
    "perPage": 10,
    "showMeticsAtAllLevels": false,
    "sort": {
      "columnIndex": 0,
      "direction": "desc"
    }
  },
  "aggs": [
    {
      "type": "terms",
      "schema": "bucket",
      "params": {
        "field": "process.keyword",
        "size": 10,
        "order": "desc"
      }
    }
  ]
}