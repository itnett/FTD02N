import com.azure.identity.DefaultAzureCredentialBuilder;
import com.azure.resourcemanager.AzureResourceManager;
import com.azure.resourcemanager.resources.models.ResourceGroup;
import com.azure.resourcemanager.resources.models.GenericResource;
import com.microsoft.graph.authentication.IAuthenticationProvider;
import com.microsoft.graph.requests.GraphServiceClient;
import okhttp3.Request;

import java.io.FileWriter;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class ComplianceCheck {
    private static AzureResourceManager azure;
    private static GraphServiceClient<Request> graphClient;

    public static void main(String[] args) throws IOException {
        authenticateAzure();
        authenticateGraph();
        
        Map<String, String> complianceResults = new HashMap<>();
        complianceResults.putAll(checkAzureResources());
        complianceResults.putAll(checkM365Services());

        try (FileWriter file = new FileWriter("compliance_result.json")) {
            file.write(complianceResults.toString());
        }
    }

    private static void authenticateAzure() {
        azure = AzureResourceManager.configure()
                .withLogLevel(HttpLogDetailLevel.BASIC)
                .authenticate(new DefaultAzureCredentialBuilder().build(), new AzureProfile(AzureEnvironment.AZURE))
                .withDefaultSubscription();
    }

    private static void authenticateGraph() {
        IAuthenticationProvider authProvider = request -> {
            request.addHeader("Authorization", "Bearer " + new DefaultAzureCredentialBuilder().build().getToken(new TokenRequestContext().addScopes("https://graph.microsoft.com/.default")).block().getToken());
        };
        graphClient = GraphServiceClient.builder().authenticationProvider(authProvider).buildClient();
    }

    private static Map<String, String> checkAzureResources() {
        Map<String, String> results = new HashMap<>();
        for (ResourceGroup rg : azure.resourceGroups().list()) {
            for (GenericResource resource : azure.genericResources().listByResourceGroup(rg.name())) {
                String complianceStatus = "Compliant"; // Placeholder logic
                if (resource.kind().equals("example-non-compliant-kind")) {
                    complianceStatus = "Non-compliant";
                }
                results.put(resource.id(), complianceStatus);
            }
        }
        return results;
    }

    private static Map<String, String> checkM365Services() {
        Map<String, String> results = new HashMap<>();
        graphClient.users().buildRequest().get().getCurrentPage().forEach(user -> {
            String complianceStatus = "Compliant"; // Placeholder logic
            if (!user.mail.contains("example-compliant-attribute")) {
                complianceStatus = "Non-compliant";
            }
            results.put(user.id, complianceStatus);
        });
        return results;
    }
}