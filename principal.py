import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# 乱数シードを設定して再現性を確保
np.random.seed(42)

# データの次元数とサンプル数
num_features = 50
num_samples = 100

# ランダムなデータを生成
data = np.random.randn(num_samples, num_features)

# 主成分分析を実行
pca = PCA()
transformed_data = pca.fit_transform(data)

# 寄与率を表示
print("Explained Variance Ratios:", pca.explained_variance_ratio_)

# 累積寄与率を計算
cumulative_variance_ratio = np.cumsum(pca.explained_variance_ratio_)

# 寄与率のグラフをプロット
plt.plot(
    range(1, num_features + 1), cumulative_variance_ratio, marker="o", linestyle="--"
)
plt.xlabel("Number of Components")
plt.ylabel("Cumulative Explained Variance Ratio")
plt.title("Cumulative Explained Variance Ratio")
plt.show()
