SELECT
    deviceId,
    AVG(humidity) AS avgHumidity,
    System.Timestamp AS eventTime
INTO
    [PowerBIOutput]
FROM
    [IoTHubInput]
GROUP BY
    deviceId,
    TumblingWindow(minute, 1)