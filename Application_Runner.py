import tkinter
import tkinter.ttk
import Info_Sorter
import File_Reader

class ApplicationRunner:
    def __init__(self):
        '''Initializer sets up the frames used to hold the top frame, side frame and main frame'''
        self._root_window = tkinter.Tk()       

        self.top_frame(self._root_window)
        self.input_frame(self._root_window)
        self.data_frame(self._root_window)

        
        
        #self.data_display(self.data_frame, sorted_info, organized_dictionary)

        self._root_window.columnconfigure(0, weight = 7)
        self._root_window.columnconfigure(0, weight = 2)

    def run(self):
        '''This will be called on to run the application'''
        self._root_window.mainloop()

    def top_frame(self, master):
        '''This frame only displays the title of the application'''
        self.top_frame = tkinter.Frame(master = self._root_window,
                                       bg = '#527F76', height = 75, width = 900)
        self.top_frame.grid(row = 0, column = 0, columnspan = 2,)

        self.title_label = tkinter.Label(master = self.top_frame,bg = '#527F76', font = ('arial', 20),
                                         fg = '#FFF',
                                         text = "Software Developers and Programmers in Various Industries")
        #self.title_label.grid(row = 0, column = 0, columnspan = 2)
        #self.title_label.columnconfigure(0, weight = 1)

        self.title_label.place(x = 450, y = 37.5, anchor = 'center')
        
        self.top_frame.grid_propagate(False)

    def input_frame(self, master):
        '''Frame used to hold user input'''
        self.input_frame = self.input_frame = tkinter.Frame(master = self._root_window,
                                         background = '#bad6cb', height = 500, width = 200)

        self.sort_label = tkinter.Label(master = self.input_frame, width = 25, bg = '#bad6cb',
                                         text = "Sort By:", font = 'arial 8 bold', anchor = 'w',
                                        justify = tkinter.LEFT)
        
        self.sort_label.grid(row = 0, column = 0, columnspan = 1)
        self.variable = tkinter.StringVar()
        self.variable.set("Select")

        self.sortOptions = ("Employment", "Annual Mean Wage","Annual Median Wage", "Hourly Mean Wage", "Hourly Median Wage")

        self.sortByMenu = tkinter.OptionMenu(self.input_frame, self.variable, *self.sortOptions)
        self.sortByMenu.config(width = 20)
        self.sortByMenu.grid(row = 1, column = 0, columnspan = 1)

        self.entry_label = tkinter.Label(master = self.input_frame, width = 25, bg = '#bad6cb',
                                         text = "Number of data entries:", font = 'arial 8 bold', anchor = 'w',
                                         justify = tkinter.LEFT)
        self.entry_label.grid(row = 2, column = 0)

        self.entry = tkinter.Text(self.input_frame, width = 20 , height = 1)
        self.entry.grid(row = 3, column = 0, columnspan = 1)

        self.submitButton = tkinter.Button(self.input_frame, text = "Submit",height = 1,
                                           width = 10, font = ('Helvetica', 16), command = self.submit_button)

        self.first_call = True
        
        self.submitButton.grid(row = 4, column = 0,)

        self.input_frame.grid_propagate(False)
        self.input_frame.grid(row = 1, column = 1,)

        workbook = File_Reader.open_file('BLS_employment_stats_may_2017.xlsx')
        worksheet = File_Reader.open_sheet(workbook, "OES Sheet")
        self.organized_dictionary = File_Reader.organize_sheet(worksheet, File_Reader.COLUMN_LIST, File_Reader.MIN_NUM, File_Reader.MAX_NUM)

    def submit_button(self):
        self.input_frame.update()
        if(self.first_call == False):
            self._data_frame.destroy()
            self.data_frame(self._root_window)
        try:
            if(self.entry.get(1.0, tkinter.END).strip().isnumeric() & (0 < int(self.entry.get(1.0, tkinter.END).strip()) < 351)):
                if(self.variable.get() != "Select"):
                    if(self.variable.get() == "Employment"):
                        self.data_display(self._data_frame, Info_Sorter.sort_by_employment(self.organized_dictionary), self.organized_dictionary, int(self.entry.get(1.0, tkinter.END).strip()))
                    elif(self.variable.get() == "Annual Mean Wage"):
                        self.data_display(self._data_frame, Info_Sorter.sort_by_annual_mean_wage(self.organized_dictionary), self.organized_dictionary, int(self.entry.get(1.0, tkinter.END).strip()))
                    elif(self.variable.get() == "Annual Median Wage"):
                        self.data_display(self._data_frame, Info_Sorter.sort_by_annual_median_wage(self.organized_dictionary), self.organized_dictionary, int(self.entry.get(1.0, tkinter.END).strip()))
                    elif(self.variable.get() == "Hourly Mean Wage"):
                        self.data_display(self._data_frame, Info_Sorter.sort_by_hourly_mean_wage(self.organized_dictionary), self.organized_dictionary, int(self.entry.get(1.0, tkinter.END).strip()))
                    else:
                        self.data_display(self._data_frame, Info_Sorter.sort_by_hourly_median_wage(self.organized_dictionary), self.organized_dictionary, int(self.entry.get(1.0, tkinter.END).strip()))
        except(Exception):
            pass
        self.first_call = False

    def data_frame(self,master):
        '''Main frame in the center used to contain all of the information'''
        self._data_frame = tkinter.Frame(master = self._root_window,
                                       background = '#FFFFFF', height = 500, width = 684)

        self._data_frame.columnconfigure(0,weight = 1)
        self._data_frame.grid_propagate(False)
        self._data_frame.grid(row = 1, column = 0)

    def data_display(self, master, ordered_occupations: list, main_dictionary: dict, entries: int):
        '''This is where the data will be displayed'''
        self.scroll_bar = tkinter.ttk.Scrollbar(master = self._data_frame)
        self.scroll_bar.pack(side = tkinter.RIGHT, fill = tkinter.Y)
        
        self._data_display = tkinter.Canvas(master = master, height = 500, width = 684,
                                           yscrollcommand = self.scroll_bar.set)
        self.scroll_bar.config(command = self._data_display.yview)

        self.new_frame = tkinter.Frame(master = self._data_display, height = 500, width = 684)

        self._data_display.pack(side = tkinter.LEFT, expand = True, fill = "both")        

        self._data_display.create_window(0,0, window = self.new_frame, anchor = 'nw')
        
        self.occupation = tkinter.Label(master = self.new_frame, bg = "#AFA", height = 2, width = 14,
                                        highlightcolor = "#FFF", highlightthickness = 5, text = "Industry")
        self.occupation.grid(row = 0, column = 0)
 
        self.employment_label = tkinter.Label(master = self.new_frame, bg = "#FAF", height = 2, width = 14,
                                         highlightcolor = "#FFF", highlightthickness = 5, text = "Employment",)
        self.employment_label.grid(row = 0, column = 1, columnspan = 1, sticky = tkinter.NW)
        
        self.annual_mean_label = tkinter.Label(master = self.new_frame, bg = "#AFA", height = 2, width = 14,
                                         highlightcolor = "#FFF", highlightthickness = 5, text = "Annual Mean\n Income")
        self.annual_mean_label.grid(row = 0, column = 2, columnspan = 1, sticky = tkinter.NW)

        self.annual_median_label = tkinter.Label(master = self.new_frame, bg = "#FAF", height = 2, width = 14,
                                        highlightcolor = "#FFF", highlightthickness = 5, text = "Annual Median\n Income")
        self.annual_median_label.grid(row = 0, column = 3, columnspan = 1, sticky = tkinter.NW) 

        self.hourly_mean_label = tkinter.Label(master = self.new_frame, bg = "#AFA", height = 2, width = 14,
                                         highlightcolor = "#FFF", highlightthickness = 5, text = "Hourly Mean\n Income")
        self.hourly_mean_label.grid(row = 0, column = 4, columnspan = 1, sticky = tkinter.NW)

        self.hourly_median_label = tkinter.Label(master = self.new_frame, bg = "#FAF", height = 2, width = 14,
                                        highlightcolor = "#FFF", highlightthickness = 5, text = "Hourly Median\n Income")
        self.hourly_median_label.grid(row = 0, column = 5, columnspan = 1, sticky = tkinter.NW)
        
        for occupation_index in range(entries):
            index_counter = 0
            for data_field in main_dictionary[ordered_occupations[occupation_index]]:
                index_counter +=1
                selected_height = len(ordered_occupations[occupation_index]) // 12
                color = ""
                
                if(occupation_index%2 == 0):
                    color = "#FAF"
                else:
                    color = "#AFA"
                

                new_label = tkinter.Label(master = self.new_frame, bg = color, height = selected_height, width = 14, wraplength = 100,
                              highlightcolor = "#FFF", highlightthickness = 5, text = ordered_occupations[occupation_index])

                if(index_counter%2 == 0):
                    color = "#bad4ff"
                else:
                    color = "#74a3f2"
                
                
                data_label = tkinter.Label(master = self.new_frame, bg = color, height = selected_height, width = 14,
                                           highlightcolor = "#FFF", highlightthickness = 5, text = main_dictionary[ordered_occupations[occupation_index]][data_field])
    
                new_label.grid(row = occupation_index+1, column = 0, columnspan = 1, sticky = tkinter.NW)
                data_label.grid(row = occupation_index+1, column = index_counter, columnspan = 1, sticky = tkinter.NW)
                
        self._data_frame.update()        
        self._data_display.config(scrollregion = self._data_display.bbox("all"))

if __name__ == '__main__': 
    ApplicationRunner().run()

