SubsetByMonth <- function(timeseries.df, set.month) {
  # Subsets a times series dataframe with a timestamp column called Date.and.Time into a month 
  # 
  # Args:
  #   timeseries.df: Time series dataframe that contains a date time column in the class of factor or character
  #   set.month: a string that is the format "YYYY-MM"
  #
  #   Returns:
  #   one.month: A dataframe that has been subset-ed to a month.  
  # Date: 1 Febuary 2019
  # Author: Andrew Chien
  # TODO(AndrewC): Need to add error handling for arguments
  
  #converts the Date.and.Time column into POSIXct Class
  timeseries.df$Date.and.Time <- as.POSIXct(timeseries.df$Date.and.Time, 
                                            format="%m/%d/%Y %H:%M:%S")
  
  #adds the string "-01 00:00:00" to complete the date as first day of the month
  startdatetime <- paste(set.month, "-01 00:00:00", sep="")
  
  #calculates the last day of set.month
  enddatetime <- (seq(as.Date(startdatetime), length=2, by="months") - 1)
  enddatetime <- enddatetime[-1]
  
  #converts the string into Date Class
  startdatetime <- as.Date(startdatetime)
  
  #subsets timeseries.df to the set startdatetime and enddatetime range
  one.month <- subset(timeseries.df,timeseries.df$Date.and.Time  > startdatetime 
                      & timeseries.df$Date.and.Time < enddatetime)
  
  # Error handling
  #TODO check if set.month argument is the correct format
  #TODO check if set.month argument is in the valid range
  
  return (one.month)
  
}