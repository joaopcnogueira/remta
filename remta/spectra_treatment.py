import pandas as pd
from sklearn.decomposition import PCA
import plotly.express as px


class SpectraTreatment:

    @staticmethod
    def plot_spectra(df: pd.DataFrame, pca=False, n_components=2):

        if pca == False:
            tidy_df = df.drop(['x', 'y'], axis=1).melt(var_name='spectro', value_name='valor')
            tidy_df['row'] = tidy_df.groupby('spectro').cumcount() + 1 

            fig = px.line(tidy_df, x='row', y='valor', color='spectro')

            return fig.show()   

        else:
            pca = PCA(n_components=n_components)
            pca_results = pca.fit_transform(df.drop(['x', 'y'], axis=1))

            pca_tidy_df = (
                pd.DataFrame(pca_results, columns=['pc1', 'pc2'])
                .melt(var_name='pc', value_name='valor')
                .assign(row = lambda df: df.groupby('pc').cumcount() + 1)
            )

            fig = px.line(pca_tidy_df, x='row', y='valor', color='pc')

            return fig.show()

