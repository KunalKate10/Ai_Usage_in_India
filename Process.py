import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("ai_tool_usage_india_synthetic.csv")
print(df)

sns.set(style="whitegrid")

plt.figure(figsize=(10, 6))
ai_tool_counts = df['AI_Tool'].value_counts()
sns.barplot(x=ai_tool_counts.values, y=ai_tool_counts.index, palette="viridis")
plt.title('Total AI Tool Usage Count')
plt.xlabel('Number of Users')
plt.ylabel('AI Tool')
plt.tight_layout()
plt.show()

# 2. Usage frequency distribution
plt.figure(figsize=(8, 5))
freq_counts = df['Usage_Frequency'].value_counts()
sns.barplot(x=freq_counts.index, y=freq_counts.values, palette="coolwarm")
plt.title('Usage Frequency Distribution')
plt.xlabel('Usage Frequency')
plt.ylabel('Number of Users')
plt.tight_layout()
plt.show()

# Count users in each age group
age_counts = df['Age_Group'].value_counts()

# Create the plot
plt.figure(figsize=(8, 5))
sns.barplot(x=age_counts.index, y=age_counts.values, palette="Set2")
plt.title('AI Tool Usage by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Number of Users')
plt.tight_layout()
plt.show()

# 3. Purpose of usage
plt.figure(figsize=(8, 5))
purpose_counts = df['Purpose'].value_counts()
sns.barplot(x=purpose_counts.index, y=purpose_counts.values, palette="Set2")
plt.title('Purpose of AI Tool Usage')
plt.xlabel('Purpose')
plt.ylabel('Number of Users')
plt.tight_layout()
plt.show()

# 4. Top 10 states using AI tools
plt.figure(figsize=(12, 6))
top_states = df['State'].value_counts().nlargest(10)
sns.barplot(y=top_states.index, x=top_states.values, palette="magma")
plt.title('Top 10 States Using AI Tools')
plt.xlabel('Number of Users')
plt.ylabel('State')
plt.show()
