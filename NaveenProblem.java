package com.java.test;

import static org.assertj.core.api.Assertions.*;
import java.time.Duration;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.DataProvider;
import org.testng.annotations.Test;
import io.github.bonigarcia.wdm.WebDriverManager;

public class NaveenProblem {
	WebDriver driver;
	WebDriverWait wait;

	@BeforeMethod
	public void beforeMethod() {
		WebDriverManager.chromedriver().setup();
		driver = new ChromeDriver();
		driver.get("https://petdiseasealerts.org/forecast-map#/heartworm-canine/dog/united-states");
		driver.manage().window().maximize();
		driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
		JavascriptExecutor js = (JavascriptExecutor) driver;
		js.executeScript("window.scrollBy(0,450)");
		driver.switchTo().frame(driver.findElement(By.xpath("//iframe[contains(@id,'map')]")));
		wait = new WebDriverWait(driver, Duration.ofSeconds(10));
	}

	@Test(dataProvider = "getData")
	public void NP(String US_States) throws Exception {

		wait.until(d -> driver.findElement(By.cssSelector("g.region")).isDisplayed());
		driver.findElements(By.cssSelector("g.region g.rpath path")).stream()
											.filter(ele -> ele.getAttribute("name").equals(US_States))
											.forEach(ele -> {
																ele.click();
																assertThat(driver.findElement(By.xpath("//ul[@class='breadcrumb']/li/span")).getText().toUpperCase())
																.isNotNull()
																.startsWith(String.valueOf(US_States.charAt(0)))
																.isEqualTo(US_States.toUpperCase());
															});
		driver.quit();

	}

	@DataProvider(name = "getData")
	public String[] supplyData() {
		return new String[] { "Texas", "Arizona", "New Mexico" };
	}

}
