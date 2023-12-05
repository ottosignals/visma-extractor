bq_schema = [
    {"name": "Id", "type": "STRING", "mode": "NULLABLE"},
    {"name": "Amount", "type": "NUMERIC", "mode": "NULLABLE"},
    {"name": "CustomerId", "type": "STRING", "mode": "NULLABLE"},
    {"name": "CurrencyCode", "type": "STRING", "mode": "NULLABLE"},
    {"name": "CreatedUtc", "type": "TIMESTAMP", "mode": "NULLABLE"},
    {"name": "VatAmount", "type": "NUMERIC", "mode": "NULLABLE"},
    {"name": "RoundingsAmount", "type": "NUMERIC", "mode": "NULLABLE"},
    {"name": "DeliveredAmount", "type": "NUMERIC", "mode": "NULLABLE"},
    {"name": "DeliveredVatAmount", "type": "NUMERIC", "mode": "NULLABLE"},
    {"name": "DeliveredRoundingsAmount", "type": "NUMERIC", "mode": "NULLABLE"},
    {"name": "DeliveryCustomerName", "type": "STRING", "mode": "NULLABLE"},
    {"name": "DeliveryAddress1", "type": "STRING", "mode": "NULLABLE"},
    {"name": "DeliveryAddress2", "type": "STRING", "mode": "NULLABLE"},
    {"name": "DeliveryPostalCode", "type": "STRING", "mode": "NULLABLE"},
    {"name": "DeliveryCity", "type": "STRING", "mode": "NULLABLE"},
    {"name": "DeliveryCountryCode", "type": "STRING", "mode": "NULLABLE"},
    {"name": "YourReference", "type": "STRING", "mode": "NULLABLE"},
    {"name": "OurReference", "type": "STRING", "mode": "NULLABLE"},
    {"name": "BuyersOrderReference", "type": "STRING", "mode": "NULLABLE"},
    {"name": "InvoiceAddress1", "type": "STRING", "mode": "NULLABLE"},
    {"name": "InvoiceAddress2", "type": "STRING", "mode": "NULLABLE"},
    {"name": "InvoiceCity", "type": "STRING", "mode": "NULLABLE"},
    {"name": "InvoiceCountryCode", "type": "STRING", "mode": "NULLABLE"},
    {"name": "InvoiceCustomerName", "type": "STRING", "mode": "NULLABLE"},
    {"name": "CustomerNumber", "type": "STRING", "mode": "NULLABLE"},
    {"name": "CustomerName", "type": "STRING", "mode": "NULLABLE"},
    {"name": "InvoicePostalCode", "type": "STRING", "mode": "NULLABLE"},
    {"name": "DeliveryMethodName", "type": "STRING", "mode": "NULLABLE"},
    {"name": "DeliveryMethodCode", "type": "STRING", "mode": "NULLABLE"},
    {"name": "DeliveryTermName", "type": "STRING", "mode": "NULLABLE"},
    {"name": "DeliveryTermCode", "type": "STRING", "mode": "NULLABLE"},
    {"name": "EuThirdParty", "type": "BOOLEAN", "mode": "NULLABLE"},
    {"name": "CustomerIsPrivatePerson", "type": "BOOLEAN", "mode": "NULLABLE"},
    {"name": "IncludesVat", "type": "BOOLEAN", "mode": "NULLABLE"},
    {"name": "OrderDate", "type": "TIMESTAMP", "mode": "NULLABLE"},
    {"name": "Status", "type": "NUMERIC", "mode": "NULLABLE"},
    {"name": "Number", "type": "NUMERIC", "mode": "NULLABLE"},
    {"name": "ModifiedUtc", "type": "TIMESTAMP", "mode": "NULLABLE"},
    {"name": "DeliveryDate", "type": "TIMESTAMP", "mode": "NULLABLE"},
    {"name": "HouseWorkAmount", "type": "NUMERIC", "mode": "NULLABLE"},
    {"name": "HouseWorkAutomaticDistribution", "type": "BOOLEAN", "mode": "NULLABLE"},
    {"name": "HouseWorkCorporateIdentityNumber", "type": "STRING", "mode": "NULLABLE"},
    {"name": "HouseWorkPropertyName", "type": "STRING", "mode": "NULLABLE"},
    {
        "name": "SalesDocumentAttachments",
        "type": "STRING",
        "mode": "REPEATED",
        "fields": [{"name": "SalesDocumentAttachment", "type": "STRING", "mode": "NULLABLE"}]
    },
    {
        "name": "MessageThreads",
        "type": "STRING",
        "mode": "REPEATED",
        "fields": [{"name": "MessageThread", "type": "STRING", "mode": "NULLABLE"}]
    },
    {
        "name": "Notes",
        "type": "STRING",
        "mode": "REPEATED",
        "fields": [{"name": "Note", "type": "STRING", "mode": "NULLABLE"}]
    },
    {
        "name": "Rows",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
            {"name": "Id", "type": "STRING", "mode": "NULLABLE"},
            {"name": "LineNumber", "type": "NUMERIC", "mode": "NULLABLE"},
            {"name": "DeliveredQuantity", "type": "NUMERIC", "mode": "NULLABLE"},
            {"name": "ArticleId", "type": "STRING", "mode": "NULLABLE"},
            {"name": "IsServiceArticle", "type": "BOOLEAN", "mode": "NULLABLE"},
            {"name": "UnitId", "type": "STRING", "mode": "NULLABLE"},
            {"name": "ArticleNumber", "type": "STRING", "mode": "NULLABLE"},
            {"name": "IsTextRow", "type": "BOOLEAN", "mode": "NULLABLE"},
            {"name": "Text", "type": "STRING", "mode": "NULLABLE"},
            {"name": "UnitPrice", "type": "NUMERIC", "mode": "NULLABLE"},
            {"name": "Amount", "type": "NUMERIC", "mode": "NULLABLE"},
            {"name": "DiscountPercentage", "type": "NUMERIC", "mode": "NULLABLE"},
            {"name": "Quantity", "type": "NUMERIC", "mode": "NULLABLE"},
            {"name": "WorkCostType", "type": "NUMERIC", "mode": "NULLABLE"},
            {"name": "IsWorkCost", "type": "BOOLEAN", "mode": "NULLABLE"},
            {"name": "WorkHours", "type": "NUMERIC", "mode": "NULLABLE"},
            {"name": "MaterialCosts", "type": "NUMERIC", "mode": "NULLABLE"},
            {"name": "EligibleForReverseChargeOnVat", "type": "BOOLEAN", "mode": "NULLABLE"},
            {"name": "CostCenterItemId1", "type": "STRING", "mode": "NULLABLE"},
            {"name": "CostCenterItemId2", "type": "STRING", "mode": "NULLABLE"},
            {"name": "CostCenterItemId3", "type": "STRING", "mode": "NULLABLE"},
            {"name": "ProjectId", "type": "STRING", "mode": "NULLABLE"},
            {"name": "GreenTechnologyType", "type": "NUMERIC", "mode": "NULLABLE"},
            {
                "name": "ContributionMargin",
                "type": "RECORD",
                "mode": "NULLABLE",
                "fields": [
                    {"name": "Amount", "type": "NUMERIC", "mode": "NULLABLE"},
                    {"name": "Percentage", "type": "NUMERIC", "mode": "NULLABLE"}
                ]
            }
        ]
    },
    {"name": "ShippedDateTime", "type": "TIMESTAMP", "mode": "NULLABLE"},
    {"name": "RotReducedInvoicingType", "type": "NUMERIC", "mode": "NULLABLE"},
    {"name": "RotReducedInvoicingPercent", "type": "NUMERIC", "mode": "NULLABLE"},
    {"name": "RotPropertyType", "type": "NUMERIC", "mode": "NULLABLE"},
    {
        "name": "Persons",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
            {"name": "Ssn", "type": "STRING", "mode": "NULLABLE"},
            {"name": "Amount", "type": "NUMERIC", "mode": "NULLABLE"}
        ]
    },
    {"name": "ReverseChargeOnConstructionServices", "type": "BOOLEAN", "mode": "NULLABLE"},
    {"name": "UsesGreenTechnology", "type": "BOOLEAN", "mode": "NULLABLE"},
    {"name": "IsNotDelivered", "type": "BOOLEAN", "mode": "NULLABLE"},
    {
        "name": "ContributionMargin",
        "type": "RECORD",
        "mode": "NULLABLE",
        "fields": [
            {"name": "Amount", "type": "NUMERIC", "mode": "NULLABLE"},
            {"name": "Percentage", "type": "NUMERIC", "mode": "NULLABLE"}
        ]
    }
]
