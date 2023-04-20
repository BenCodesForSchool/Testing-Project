export default class InvoicePage {
  private INVOICE_BUTTON = "//a[@class='btn btn-default check_out']";
  private LOGOUT_BUTTON = './/a[@href="/logout"]';

  downloadInvoice(): void {
    cy.xpath(this.INVOICE_BUTTON).click();

    // Logging out exclusively for the purpose of running the test case recommended by Tyler
    cy.xpath(this.LOGOUT_BUTTON).click();
  }

  assertInvoiceDownloaded(): void {
    const filePath = "D:\\C DRIVE STUFF\\Downloads\\invoice.txt";

    // Assert that the file exists and is not empty
    cy.task("fileExists", filePath).should("eq", true);
    cy.task("fileSize", filePath).should("be.greaterThan", 0);
  }
}
