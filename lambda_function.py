import boto3
import csv
import io
from urllib.parse import unquote_plus

s3 = boto3.client("s3")

DESTINATION_BUCKET = "cana-week4-processed-data-2026"

def lambda_handler(event, context):
    for record in event["Records"]:
        source_bucket = record["s3"]["bucket"]["name"]
        source_key = unquote_plus(record["s3"]["object"]["key"])

        response = s3.get_object(
            Bucket=source_bucket,
            Key=source_key
        )

        content = response["Body"].read().decode("utf-8-sig")
        input_file = io.StringIO(content)
        reader = csv.DictReader(input_file)

        output_file = io.StringIO()

        fieldnames = [
            "transaction_id",
            "product",
            "quantity",
            "unit_price",
            "total"
        ]

        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            try:
                transaction_id = row["transaction_id"].strip()
                product = row["product"].strip()
                quantity = int(row["quantity"])
                unit_price = float(row["unit_price"])

                if not transaction_id or not product:
                    continue

                if quantity <= 0 or unit_price < 0:
                    continue

                writer.writerow({
                    "transaction_id": transaction_id,
                    "product": product,
                    "quantity": quantity,
                    "unit_price": f"{unit_price:.2f}",
                    "total": f"{quantity * unit_price:.2f}"
                })

            except (ValueError, KeyError, TypeError):
                continue

        output_key = "processed/" + source_key.split("/")[-1]

        s3.put_object(
            Bucket=DESTINATION_BUCKET,
            Key=output_key,
            Body=output_file.getvalue().encode("utf-8"),
            ContentType="text/csv"
        )

    return {
        "statusCode": 200,
        "body": "CSV file processed successfully"
    }
