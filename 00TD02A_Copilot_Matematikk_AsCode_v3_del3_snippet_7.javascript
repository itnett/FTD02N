// Create the collection and insert data
db.PerformanceMetrics.insert({
    student_id: 1,
    cpu_usage: 75.5,
    memory_usage: 60.2,
    network_traffic: 500.0,
    disk_usage: 250.0,
    network_latency: 20.5
});

// Query to calculate percentage utilization
db.PerformanceMetrics.aggregate([
    {
        $project: {
            student_id: 1,
            percentage_utilization: {
                $multiply: [
                    {
                        $divide: [
                            { $add: ["$cpu_usage", "$memory_usage"] },
                            2
                        ]
                    },
                    100
                ]
            }
        }
    }
]);