import matplotlib.pyplot as plt
sentiment = [589,411,555,555,555]
bin_width = 10
kelompok_interval = range(0,1000 + bin_width,bin_width)
plt.hist(sentiment,kelompok_interval)
plt.show()