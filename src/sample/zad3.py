import math
import unittest


def statement(invoice, plays):
    total_amount = 0
    volume_credits = 0
    result = f'Statement for {invoice["customer"]}\n'

    def format_as_dollars(amount):
        return f"${amount:0,.2f}"

    for perf in invoice['performances']:
        play = plays[perf['playID']]
        if play['type'] == "tragedy":
            this_amount = 40000
            if perf['audience'] > 30:
                this_amount += 1000 * (perf['audience'] - 30)
        elif play['type'] == "comedy":
            this_amount = 30000
            if perf['audience'] > 20:
                this_amount += 10000 + 500 * (perf['audience'] - 20)

            this_amount += 300 * perf['audience']

        else:
            raise ValueError(f'unknown type: {play["type"]}')

        # add volume credits
        volume_credits += max(perf['audience'] - 30, 0)
        # add extra credit for every ten comedy attendees
        if "comedy" == play["type"]:
            volume_credits += math.floor(perf['audience'] / 5)
        # print line for this order
        result += f' {play["name"]}: {format_as_dollars(this_amount / 100)} ({perf["audience"]} seats)\n'
        total_amount += this_amount

    result += f'Amount owed is {format_as_dollars(total_amount / 100)}\n'
    result += f'You earned {volume_credits} credits\n'
    return result


"""
Invoice.json
{
  "customer": "BigCo",
  "performances": [
    {
      "playID": "hamlet",
      "audience": 55
    },
    {
      "playID": "as-like",
      "audience": 35
    },
    {
      "playID": "othello",
      "audience": 40
    }
  ]
}

Plays.json
{
  "hamlet": {"name": "Hamlet", "type": "tragedy"},
  "as-like": {"name": "As You Like It", "type": "comedy"},
  "othello": {"name": "Othello", "type": "tragedy"}
}
"""


class Test_Statement(unittest.TestCase):
    plays = {
        "hamlet": {"name": "Hamlet", "type": "tragedy"},
        "as-like": {"name": "As You Like It", "type": "comedy"},
        "othello": {"name": "Othello", "type": "tragedy"},
        "lolo": {"name": "Lolo", "type": "thriller"}
    }

    def test_tragedy_with_audience_lower_than_30(self):
        invoice = {
            "customer": "BigCo",
            "performances": [
                {
                    "playID": "othello",
                    "audience": 20
                }
            ]
        }
        result = "Statement for BigCo\n Othello: $400.00 (20 seats)\nAmount owed is $400.00\nYou earned 0 credits\n"
        self.assertEqual(statement(invoice, self.plays), result)

    def test_comedy_with_audience_60(self):
        invoice = {
            "customer": "BigCo",
            "performances": [
                {
                    "playID": "as-like",
                    "audience": 60
                }
            ]
        }
        result = "Statement for BigCo\n As You Like It: $780.00 (60 seats)\nAmount owed is $780.00\nYou earned 42 credits\n"
        self.assertEqual(statement(invoice, self.plays), result)

    def test_tragedy_audience_higher_than_30(self):
        invoice = {
            "customer": "BigCo",
            "performances": [
                {
                    "playID": "hamlet",
                    "audience": 70
                }
            ]
        }
        result = "Statement for BigCo\n Hamlet: $800.00 (70 seats)\nAmount owed is $800.00\nYou earned 40 credits\n"
        self.assertEqual(statement(invoice, self.plays), result)

    def test_unknown_type(self):
        invoice = {
            "customer": "BigCo",
            "performances": [
                {
                    "playID": "lolo",
                    "audience": 1234
                }
            ]
        }
        with self.assertRaises(ValueError):
            statement(invoice, self.plays)


if __name__ == "__main__":
    unittest.main()
