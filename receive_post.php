<?php
// Get raw POST data
$rawData = file_get_contents("php://input");

// Decode JSON data
$jsonData = json_decode($rawData, true);

// Prepare log file path
$logFile = '/var/log/apache2/post_requests.log';
$logEntry = "Received at " . date('Y-m-d H:i:s') . ": " . print_r($jsonData, true) . "\n";

// Log the data to the file
if (file_put_contents($logFile, $logEntry, FILE_APPEND) === false) {
    // Log error if file_put_contents fails
    error_log("Failed to write to log file.");
}

// Respond to the client
echo json_encode(["status" => "success", "data" => $jsonData]);
?>