import { v4 as uuidv4 } from "uuid";

describe("Checkout v2, Cloud Scaler Monthly", () => {
  const email = `testing-${uuidv4()}@printnanny.ai`;
  let checkoutRedirectUrl = "";

  const billingName = "Wile E Coyote";
  const address1 = "747 Howard St";
  const city = "San Francisco";
  const zip = "94107";

  const price = "$19.99";
  const cardNumber = "4242 4242 4242 4242";
  const exp = "05/25";
  const cvc = "123";
  const phoneNumber = "8888675309";

  const promotionCode = "FOUNDING10";

  it("Should redirect to Stripe Checkout session for monthly Cloud Scaler plan", () => {
    cy.visit("/pricing");

    cy.get("button#pricing-monthly-toggle").click();
    cy.get("a#cloud-scaler-plan-monthly").click();
    cy.url().should("contain", "/shop/checkout/cloud-scaler-plan/monthly");
    cy.get("input#email")
      .click()
      .type(email)
      .get("button[type=submit]")
      .click().then(() => {
        const sentArgs = {
          email,
          checkoutRedirectUrl,
          billingName,
          address1,
          city,
          zip,
          cardNumber,
          cvc,
          exp,
          promotionCode,
          phoneNumber,
          price
        };
        cy.origin(
          "https://checkout.stripe.com",
          { args: sentArgs },
          ({
            billingName,
            address1,
            city,
            zip,
            cardNumber,
            cvc,
            exp,
            promotionCode,
            phoneNumber,
            price
          }) => {
            cy.on("uncaught:exception", (err) => {
              if (
                err.message.includes("paymentRequest Element didn't mount normally")
              ) {
                return false;
              }
            });

            cy.contains(price);
            cy.get("input[name=cardCvc]").type(cvc.slice(0));
            cy.get("input[name=cardCvc]").type(cvc.slice(1));
            cy.get("input[name=cardCvc]").type(cvc.slice(2));

            cy.get("input[name=cardExpiry]").type(exp);
            cy.get("input[name=cardNumber]").type(cardNumber);
            cy.get("input[name=billingName]").type(billingName);
            cy.get("input[name=billingAddressLine1]")
              .type(address1)
              .type("{enter}");
            cy.get("input[name=billingLocality]").type(city);
            cy.get("input[name=billingPostalCode]").type(zip).type("{enter}");
            cy.get("input[name=enableStripePass]").check();

            cy.get("input[name=phoneNumber]").type(phoneNumber);
            cy.get("button[type=submit]", { timeout: 60000 })
              .should("have.class", "SubmitButton--complete")
              .click()
              .contains("Processing");
          }
        );
        cy.url({ timeout: 80000 }).should("contain", "/shop/thank-you/");
        cy.contains(billingName, { timeout: 10000 });
        cy.contains(address1, { timeout: 10000 });
        cy.contains(city, { timeout: 10000 });
        cy.contains(zip, { timeout: 10000 });
      });
  });

  it("Should log into cloud dashboard", () => {
    cy.session(email, () => {
      cy.loginUserWithMagicLink(email);
      cy.visit(checkoutRedirectUrl);
      cy.get("a#nav-dashboard", { timeout: 10000 })
        .click()
        .then(() =>
          cy
            .url({ timeout: 2000 })
            .should("contain", "/devices")
            .then(() => {
              cy.get("button#pn-navmenu-button", { timeout: 10000 }).click();
              cy.get(".pn-achievement-badge", { timeout: 10000 }).contains(
                "Cloud Scaler"
              );
            })
        );
    });
  });

});

describe("Checkout v2, Cloud Scaler Yearly", () => {
  const email = `testing-${uuidv4()}@printnanny.ai`;
  let checkoutRedirectUrl = "";

  const price = "$199.99";
  const billingName = "Wile E Coyote";
  const address1 = "747 Howard St";
  const city = "San Francisco";
  const zip = "94107";

  const cardNumber = "4242 4242 4242 4242";
  const exp = "05/25";
  const cvc = "123";
  const phoneNumber = "8888675309";

  const promotionCode = "FOUNDING10";

  it("Should redirect to Stripe Checkout session for yearly Cloud Scaler plan", () => {
    cy.visit("/pricing");

    cy.get("button#pricing-yearly-toggle").click();
    cy.get("a#cloud-scaler-plan-yearly").click();
    cy.url().should("contain", "/shop/checkout/cloud-scaler-plan/yearly");
    cy.get("input#email")
      .click()
      .type(email)
      .get("button[type=submit]")
      .click().then(() => {
        const sentArgs = {
          email,
          checkoutRedirectUrl,
          billingName,
          address1,
          city,
          zip,
          cardNumber,
          cvc,
          exp,
          promotionCode,
          phoneNumber,
          price
        };
        cy.origin(
          "https://checkout.stripe.com",
          { args: sentArgs },
          ({
            billingName,
            address1,
            city,
            zip,
            cardNumber,
            cvc,
            exp,
            promotionCode,
            phoneNumber,
            price
          }) => {
            cy.on("uncaught:exception", (err) => {
              if (
                err.message.includes("paymentRequest Element didn't mount normally")
              ) {
                return false;
              }
            });
            cy.contains(price);
            cy.get("input[name=cardCvc]").type(cvc.slice(0));
            cy.get("input[name=cardCvc]").type(cvc.slice(1));
            cy.get("input[name=cardCvc]").type(cvc.slice(2));

            cy.get("input[name=cardExpiry]").type(exp);
            cy.get("input[name=cardNumber]").type(cardNumber);
            cy.get("input[name=billingName]").type(billingName);
            cy.get("input[name=billingAddressLine1]")
              .type(address1)
              .type("{enter}");
            cy.get("input[name=billingLocality]").type(city);
            cy.get("input[name=billingPostalCode]").type(zip).type("{enter}");
            cy.get("input[name=enableStripePass]").check();

            cy.get("input[name=phoneNumber]").type(phoneNumber);
            cy.get("button[type=submit]", { timeout: 60000 })
              .should("have.class", "SubmitButton--complete")
              .click()
              .contains("Processing");
          }
        );
        cy.url({ timeout: 80000 }).should("contain", "/shop/thank-you/");
        cy.contains(billingName, { timeout: 10000 });
        cy.contains(address1, { timeout: 10000 });
        cy.contains(city, { timeout: 10000 });
        cy.contains(zip, { timeout: 10000 });
      });
  });

  it("Should log into cloud dashboard", () => {
    cy.session(email, () => {
      cy.loginUserWithMagicLink(email);
      cy.visit(checkoutRedirectUrl);
      cy.get("a#nav-dashboard", { timeout: 10000 })
        .click()
        .then(() =>
          cy
            .url({ timeout: 2000 })
            .should("contain", "/devices")
            .then(() => {
              cy.get("button#pn-navmenu-button", { timeout: 10000 }).click();
              cy.get(".pn-achievement-badge", { timeout: 10000 }).contains(
                "Cloud Scaler"
              );
            })
        );
    });
  });

});
