import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Optional;

public class SystemSecretManager {
    public static void main(String[] args) {
        if (args.length != 1) {
            System.err.println("Usage: 'java SystemSecretManager <secret/path>'");
            System.exit(1);
        }
        var optionalSecret = SystemSecretManager.secret(args[0]);
        if (optionalSecret.isPresent()) {
            System.out.println(optionalSecret.get());
        } else {
            System.out.println("No secret!");
        }
    }

    public static Optional<String> secret(String secretString) {
        Optional<String> secret = Optional.empty();

        try {
            var processCmd = String.format("pass %s", secretString);
            var processBuilder = new ProcessBuilder().command("bash", "-c", processCmd);
            var process = processBuilder.start();
            
            byte[] output = process.getInputStream().readAllBytes();
            int exitCode = process.waitFor();
            boolean passSuccess = (exitCode == 0);

            if (passSuccess) {
                String sec = new String(output, StandardCharsets.UTF_8).trim();
                secret = Optional.ofNullable(sec);
            }
        } catch (IOException | InterruptedException e) {
            System.out.println(e.getMessage());
        }

        return secret;
    }
}
