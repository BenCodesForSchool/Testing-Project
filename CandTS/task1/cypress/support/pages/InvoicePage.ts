export default class InvoicePage {
    private INVOICE_BUTTON = "a[class='btn btn-default check_out']";
    private LOGOUT_BUTTON = 'a[href="/logout"]';

    downloadInvoice(): void {
        cy.window().then((win) => {
            const downloadButton = cy.get(this.INVOICE_BUTTON);
            win.document.addEventListener('click', function clickListener() {
                win.document.removeEventListener('click', clickListener);
                setTimeout(() => win.location.reload(), 5000);
            });
            downloadButton.click({force: true});
        });
    }
    assertInvoiceDownloaded(): void {
        const fileName = "invoice.txt";
        const downloadFolder = 'cypress/downloads/';
        const filePath = `${downloadFolder}/${fileName}`;
  
        // Wait for the file to be downloaded before attempting to read it
        cy.wait(1500);
  
        // Read the contents of the downloaded file
        cy.readFile(filePath).then((fileContent) => {
            // Assert that the file is not empty
            expect(fileContent.trim().length).to.be.greaterThan(0);
        });
    }
}
