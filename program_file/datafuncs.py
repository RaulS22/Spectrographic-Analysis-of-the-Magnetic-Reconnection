import pandas as pd
import pywt
import plotly.graph_objs as go
from datetime import datetime, timedelta

#Funções

def fundir_colunas(row):
    return (str(row['col2']) + str(row['coltemp2']) + str(row['coltemp3']))

def Bz_denoiser(Bz, threshold):
  noisy_signal = Bz['Bz']

  # Perform a multi-level wavelet decomposition
  coeffs = pywt.wavedec(noisy_signal, 'db1', level=4)
  # Set a threshold to nullify smaller coefficients (assumed to be noise)
  coeffs_thresholded = [pywt.threshold(c, threshold, mode='soft') for c in coeffs]

  # Reconstruct the signal from the thresholded coefficients
  return pywt.waverec(coeffs_thresholded, 'db1')

def data_treatment(df):
  def convert_numeric_to_date(numeric_value):
    # Parse the numeric value into days, hours, and minutes
    days = numeric_value // 10000
    hours_minutes = numeric_value % 10000
    hours = hours_minutes // 100
    minutes = hours_minutes % 100

    # Create a reference date (e.g., January 1st of the current year)
    current_year = int(df['col1'][0])
    reference_date = datetime(current_year - 1, 12, 31)

    # Add the parsed values to the reference date
    result_date = reference_date + timedelta(days=days, hours=hours, minutes=minutes)

    # Format the result date as "dd/MMM" (e.g., "06/Jun")
    formatted_result = result_date.strftime("%d/%b")

    return formatted_result

  df.columns = ['Dados']
  df[['col1', 'col2', 'coltemp2', 'coltemp3', 'Bz']] = df['Dados'].str.split('\\s+', expand=True)
  df.pop('Dados')
  df['coltemp3'], df['coltemp2'] = df['coltemp3'].astype(str).str.zfill(2), df['coltemp2'].astype(str).str.zfill(2)
  df['col2'] = df.apply(fundir_colunas, axis=1)
  df.pop('coltemp2')
  df.pop('coltemp3')
  df['Bz'] = df['Bz'].astype(float)
  df['col2'] = df['col2'].astype(float)
  df['Bz'] = df['Bz'].replace(9999.99, None)

  df['DD/MMM'] = df['col2'].apply(convert_numeric_to_date)

  return df

def Bz_data_processer(filepath, graphs, name):

    df = pd.read_csv(open(filepath))

    df = data_treatment(df)

    denoised_ace = Bz_denoiser(df, 15)

    if graphs == True:
      """DF PLOT"""

      fig = go.Figure()

      fig.add_scatter(x=df['DD/MMM'], y=df['Bz'], mode='lines')

      fig.update_xaxes(title_text='Time')

      fig.update_yaxes(title_text='Bz')

      fig.update_layout(title= name + ' Bz vector component in data time span')

      fig.update_xaxes(showgrid=True)
      fig.update_yaxes(showgrid=True)

      fig.update_xaxes(tickangle=45)

      fig.show()

      """DF DENOISING"""

      fig = go.Figure()

      fig.add_scatter(x=df['DD/MMM'], y = denoised_ace, mode='lines')

      fig.update_xaxes(title_text='Time')

      fig.update_yaxes(title_text='Bz')

      fig.update_layout(title= 'Denoised ' + name + ' Bz vector component in data time span')

      fig.update_xaxes(showgrid=True)
      fig.update_yaxes(showgrid=True)

      fig.update_xaxes(tickangle=45)

      fig.show()

    return df, denoised_ace

def combiner(df1, denoised_df1, df2, denoised_df2, df3, denoised_df3):
  """##COMBINAÇÂO DAS 2 def"""

  # Assuming you have already created a Plotly figure or subplot
  fig = go.Figure()

  # Add a scatter or line trace for your data (replace 'x' and 'y' with your data)
  # Example:
  fig.add_scatter(x=df1['DD/MMM'], y=denoised_df1, mode='lines')
  fig.add_scatter(x=df2['DD/MMM'], y=denoised_df2, mode='lines')

  try:
    fig.add_scatter(x=df3['DD/MMM'], y=denoised_df3, mode='lines')

  except:
     pass

  # Set x-axis label
  fig.update_xaxes(title_text='Time')

  # Set y-axis label
  fig.update_yaxes(title_text='IMF Bz')

  # Set title
  fig.update_layout(title='Overlapped Bz components')

  # Enable grid lines
  fig.update_xaxes(showgrid=True)
  fig.update_yaxes(showgrid=True)

  fig.update_xaxes(tickangle=45)

  # Show the Plotly figure
  fig.show()