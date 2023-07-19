import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def plot_accuracy_all_systems():
    df = pd.read_csv("correctness_tests/benchmark_results.tsv", sep="\t")

    # Only keep the systems reynolds, russtress, random, russiangram_with_yo_fixed, russ, tempdb_3_with_ruwikipedia
    df = df[
        df["System"].isin(
            [
                "reynolds",
                "russtress",
                "random",
                "russiangram_with_yo_fixed",
                "russ",
                "tempdb_3_with_ruwikipedia",
            ]
        )
    ]

    # Rename the system names
    df["System"] = df["System"].replace(
        {
            "reynolds": "Reynolds",
            "russtress": "Russtress",
            "random": "Random",
            "russiangram_with_yo_fixed": "RussianGram",
            "russ": "Russ",
            "tempdb_3_with_ruwikipedia": "Our system",
        }
    )

    # Sort the dataframe by the percentage of correct words
    df = df.sort_values(by="Percentage correct words", ascending=True)

    # Make the size of the font on the x-axis smaller
    plt.rcParams.update({"font.size": 9})

    
    sns.barplot(data=df, x="System", y="Percentage correct words")

    plt.savefig("correctness_tests/accuracy_all_systems.png", dpi=500)

    # Plot the percentage of unstressed words
    plt.clf()
    sns.barplot(data=df, x="System", y="Percentage unstressed words")
    plt.savefig("correctness_tests/unstressed_all_systems.png", dpi=500)

    # Plot the percentage of incorrect words
    plt.clf()
    sns.barplot(data=df, x="System", y="Percentage incorrect words")
    plt.savefig("correctness_tests/incorrect_all_systems.png", dpi=500)


def filter_relevant_columns_for_latex(df: pd.DataFrame) -> pd.DataFrame:
    filtered = df[["System", "Percentage correct words", "Percentage unstressed words",	"Percentage incorrect words"]]
    # Rename the columns
    filtered = filtered.rename(
        columns={
            "Percentage correct words": "% Correct",
            "Percentage unstressed words": "% Unstressed",
            "Percentage incorrect words": "% Incorrect",
        }
    )
    return filtered


def plot_accuracy_my_systems():
    df = pd.read_csv("correctness_tests/benchmark_results.tsv", sep="\t")

    # Only keep the rows with the system columns
    # equal to tempdb_0_enwiktionary_only, tempdb_1_with_openrussian, tempdb_2_with_ruwiktionary, tempdb_3_with_ruwikipedia

    df = df[
        df["System"].isin(
            [
                "tempdb_0_enwiktionary_only",
                "tempdb_1_with_openrussian",
                "tempdb_2_with_ruwiktionary",
                "tempdb_3_with_ruwikipedia",
            ]
        )
    ]

    # Rename the system names
    df["System"] = df["System"].replace(
        {
            "tempdb_0_enwiktionary_only": "EnWiktionary",
            "tempdb_1_with_openrussian": "EnWikt + OpenRussian",
            "tempdb_2_with_ruwiktionary": "EnWikt + OR + RuWiktionary",
            "tempdb_3_with_ruwikipedia": "EnWikt + OR + RuWikt + RuWiki",
        }
    )

    sns.set(style="whitegrid")

    bp = sns.barplot(data=df, x="System", y="Percentage correct words", hue="System", dodge=False)
    #bp.legend_.remove()
    bp.legend(loc="lower right")

    bp.set(xticklabels=[])

    # Rotate x-axis labels

    plt.savefig("correctness_tests/accuracy_my_systems.png", dpi=400)
    plt.savefig("correctness_tests/accuracy_my_systems.svg")

    # Print to latex
    print(filter_relevant_columns_for_latex(df).to_latex(index=False))

    # Now calculate the change of the percentage compared to the previous system
    # and print it to latex
    df["Diff correct"] = df["Percentage correct words"].diff()
    df["Diff correct"] = df["Diff correct"].fillna(0)
    df["Diff unstressed"] = df["Percentage unstressed words"].diff()
    df["Diff unstressed"] = df["Diff unstressed"].fillna(0)
    df["Diff incorrect"] = df["Percentage incorrect words"].diff()
    df["Diff incorrect"] = df["Diff incorrect"].fillna(0)

    # Print to latex
    diff_df = df[["System", "Diff correct", "Diff unstressed", "Diff incorrect"]]
    diff_df = diff_df.rename(
        columns={
            "Diff correct": "Δ % Correct",
            "Diff unstressed": "Δ % Unstressed",
            "Diff incorrect": "Δ % Incorrect",
        }
    )
    print(diff_df.to_latex(index=False))

    # Now divide the diff correct by the diff incorrect
    diff_df["Diff correct / incorrect"] = diff_df["Δ % Correct"] / diff_df["Δ % Incorrect"]
    print(diff_df)    


def plot_chatgpt_minibenchmark():
    raise NotImplementedError

if __name__ == "__main__":
    #plot_accuracy_all_systems()
    plot_accuracy_my_systems()
