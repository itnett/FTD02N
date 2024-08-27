<?php
require 'vendor/autoload.php';

use Microsoft\Graph\Graph;
use Microsoft\Graph\Model;
use League\OAuth2\Client\Provider\GenericProvider;

function authenticateGraph() {
    $provider = new GenericProvider([
        'clientId'                => 'YOUR_APP_ID',
        'clientSecret'            => 'YOUR_APP_SECRET',
        'redirectUri'             => 'http://localhost/callback',
        'urlAuthorize'            => 'https://login.microsoftonline.com/YOUR_TENANT_ID/oauth2/v2.0/authorize',
        'urlAccessToken'          => 'https://login.microsoftonline.com/YOUR_TENANT_ID/oauth2/v2.0/token',
        'urlResourceOwnerDetails' => '',
        'scopes'                  => 'https://graph.microsoft.com/.default'
    ]);

    return $provider->getAccessToken('client_credentials');
}

function checkM365Services($accessToken) {
    $graph = new Graph();
    $graph->setAccessToken($accessToken);

    $users = $graph->createRequest("GET", "/users")
                   ->setReturnType(Model\User::class)
                   ->execute();

    $complianceResults = [];
    foreach ($users as $user) {
        $complianceStatus = strpos($user->getMail(), 'example-compliant-attribute') !== false ? 'Compliant' : 'Non-compliant';
        $complianceResults[$user->getId()] = $complianceStatus;
    }
    return $complianceResults;
}

function main() {
    $accessToken = authenticateGraph();
    $results = checkM365Services($accessToken);

    file_put_contents('compliance_result.json', json_encode($results));
}

main();
?>