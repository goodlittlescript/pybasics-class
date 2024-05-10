# DATE	    OPEN	HIGH	LOW	    CLOSE
data_str = """
05/02/24	5049.32	5073.21	5011.05	5064.20
05/01/24	5029.03	5096.12	5013.45	5018.39
04/30/24	5103.78	5110.83	5035.31	5035.69
04/29/24	5114.13	5123.49	5088.65	5116.17
04/26/24	5084.65	5114.62	5073.14	5099.96
04/25/24	5019.88	5057.75	4990.58	5048.42
04/24/24	5084.86	5089.48	5047.02	5071.63
04/23/24	5028.85	5076.12	5027.96	5070.55
04/22/24	4987.33	5038.84	4969.40	5010.60
04/19/24	5005.44	5019.02	4953.56	4967.23
04/18/24	5031.52	5056.66	5001.89	5011.12
04/17/24	5068.97	5077.96	5007.25	5022.21
04/16/24	5064.59	5079.84	5039.83	5051.41
04/15/24	5149.67	5168.43	5052.47	5061.82
04/12/24	5171.51	5175.03	5107.94	5123.41
04/11/24	5172.95	5211.78	5138.77	5199.06
04/10/24	5167.88	5178.43	5138.70	5160.64
04/09/24	5217.03	5224.81	5160.78	5209.91
04/08/24	5211.37	5219.57	5197.35	5202.39
04/05/24	5158.95	5222.18	5157.21	5204.34
04/04/24	5244.05	5256.59	5146.06	5147.21
""".strip()

#
# Python provides several list-oriented methods
# for common operations.
#

close_prices = []
for line in data_str.split("\n"):
    date_str, open_str, high_str, low_str, close_str = line.split()
    open_price = float(open_str)
    high_price = float(high_str)
    low_price = float(low_str)
    close_price = float(close_str)

    close_prices.append(close_price)

print(max(close_prices))
print(min(close_prices))

#
# ... other list-oriented methods ...
#

# print(sum(close_prices))
# print(len(close_prices))
# print(sum(close_prices) / len(close_prices))
# print(sorted(close_prices))
