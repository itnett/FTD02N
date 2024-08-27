// Create the table
r.db('test').tableCreate('PerformanceMetrics');

// Insert data
r.table('PerformanceMetrics').insert({
    student_id: 1,
    cpu_usage: 75.5,
    memory_usage: 60.2,
    network_traffic: 500.0,
    disk_usage: 250.0,
    network_latency: 20.5
});

// Query to calculate percentage utilization
r.table('PerformanceMetrics').map(function (metric) {
    return {
        student_id: metric('student_id'),
        percentage_utilization: ((metric('cpu_usage').add(metric('memory_usage'))).div(2)).mul(100)
    };
});