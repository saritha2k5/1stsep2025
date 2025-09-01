package Demo_package;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class Api_testing_page {
    public static void main(String[] args) {

        // ✅ Set path to chromedriver.exe (correct way: key + value)
        System.setProperty("webdriver.chrome.driver",
                "C:\\Users\\Hp\\eclipse-workspace\\chromedriver-win64\\chromedriver.exe");

        // 1. Launch browser
        WebDriver driver = new ChromeDriver();

        // Maximize browser window
        driver.manage().window().maximize();

        // 2. Navigate to url 'http://automationexercise.com/products'
        driver.get("https://www.automationexercise.com/api_list");

        // 3. Verify that Products page is visible successfully
        String pageTitle = driver.getTitle();
        if (pageTitle.contains("API Testing")) {
            System.out.println("✅Api testing page is visible successfully.");
        } else {
            System.out.println("❌Api testing is NOT visible.");
        }

        // Close browser
        driver.quit();
    }
}