import requests
import json 
import pandas as pd
from pandas.io.json import json_normalize
from google.cloud import bigquery


print(type(2))
print(type(str))


def read_kaggle_data():
    response  =  requests.get("https://www.kaggle.com/datasets/zalando-research/fashionmnist?resource=download&select=fashion-mnist_test.csv")
    fashion_json = response.json()
    print(fashion_json)
    # df = pd.DataFrame(fashion_json)
    # print(df.head())


def read_bigquery_data():
	client = bigquery.Client()

	sql = """
	WITH
	  TopTermsByDate AS (
	    SELECT DISTINCT refresh_date AS date, term
	    FROM `bigquery-public-data.google_trends.top_terms`
	  ),
	  DistinctDates AS (
	    SELECT DISTINCT date
	    FROM TopTermsByDate
	  )
	SELECT
	  DATE_DIFF(Dates2.date, Date1Terms.date, DAY)
	    AS days_apart,
	  COUNT(DISTINCT (Dates2.date || Date1Terms.date))
	    AS num_date_pairs,
	  COUNT(Date1Terms.term) AS num_date1_terms,
	  SUM(IF(Date2Terms.term IS NOT NULL, 1, 0))
	    AS overlap_terms,
	  SAFE_DIVIDE(
	    SUM(IF(Date2Terms.term IS NOT NULL, 1, 0)),
	    COUNT(Date1Terms.term)
	    ) AS pct_overlap_terms
	FROM
	  TopTermsByDate AS Date1Terms
	CROSS JOIN
	  DistinctDates AS Dates2
	LEFT JOIN
	  TopTermsByDate AS Date2Terms
	  ON
	    Dates2.date = Date2Terms.date
	    AND Date1Terms.term = Date2Terms.term
	WHERE
	  Date1Terms.date <= Dates2.date
	GROUP BY
	  days_apart

	ORDER BY
	  days_apart;
	"""
	pct_overlap_terms_by_days_apart = client.query(sql).to_dataframe()

	pct_overlap_terms_by_days_apart.head()


if __name__ == "__main__":
	read_data_in()