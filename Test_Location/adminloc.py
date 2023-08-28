class Adminlocation:
    #usermanagement
    user_management='//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span' #Xpath
    users='/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li/a' #Xpath
    useredit='/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[6]/div/button[2]/i'
    usersave='/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'

    #job
    job='//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span'
    #job='//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]' #Xpath
    job_title='//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[1]/a' #Xpath
    job_titleedit='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[1]/div/button'
    job_title_input='/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/input'
    savetitle='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[5]/button[2]'
    
    pay_grades='//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[2]/a' #xpath
    pay_name='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/input'
    payadd='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[1]/div/button'
    paycuradd='//*[@id="app"]/div[1]/div[2]/div[2]/div[2]/div/div[1]/div/button/i'
    curencyinput='//*[@id="app"]/div[1]/div[2]/div[2]/div[2]/form/div[1]/div/div/div/div[2]/div/div/div[1]'
    rupees='//*[@id="app"]/div[1]/div[2]/div[2]/div[2]/form/div[1]/div/div/div/div[2]/div/div[2]/div[59]'
    savepay='//*[@id="app"]/div[1]/div[2]/div[2]/div[1]/div/form/div[2]/button[2]'
    savecurrency='//*[@id="app"]/div[1]/div[2]/div[2]/div[2]/form/div[3]/button[2]'

    
    employment_status='//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[3]/a' #Xpath
    addemp='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[1]/div/button'
    emp_input='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/input'
    empsave='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'


    #job_categories='//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[4]/a' #Xpath
    job_categories='/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[4]/a'
    catadd='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[1]/div/button'
    categoryinput='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/input'
    catsave='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'

    workshifts='//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[5]/a' #Xpath
    workadd='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[1]/div/button'
    shiftinput='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/input'
    shiftsave='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[4]/button[2]'

  
    #organization
    organization='//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/span' #Xpath
    general_info='/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[1]/a' #Xpath
    editcheck='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div/label/span'
    infosave='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[7]/button'

    location='/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[2]' #XPATH
    locadd='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/button'
    locname_input='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/input'
    loccountry='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[4]/div/div[2]/div/div'
    india='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[4]/div/div[2]/div/div[2]/div[100]'
    locsave='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]'

    structure='/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[3]/a' #xpath
    strucedit='/html/body/div/div[1]/div[2]/div[2]/div/div/div[1]/div/label/span'
    strucadd='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[2]/button'
    strucname_input='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div/div/div/form/div[2]/div/div[2]/input'
    structsave='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div/div/div/form/div[4]/button[2]'


    #qualification
    qualifications='//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]/span' #Xpath
    skills='/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[4]/ul/li[1]/a' #Xpath
    skilladd='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[1]/div/button'
    skill_input='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/input'
    skillsave='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]'

    education='/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[4]/ul/li[2]/a' #Xpath
    eduadd='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[1]/div/button'
    eduinput='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/input'
    edusave= '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'

    licenses='/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[4]/ul/li[3]/a' #Xpath
    licenadd='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[1]/div/button'
    liceninput='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/input'
    licensave='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'

    languages='/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[4]/ul/li[4]/a' #Xpath
    langadd='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[1]/div/button'
    langinput='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/input'
    langsave='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'


    memberships='/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[4]/ul/li[5]/a' #Xpath
    memadd='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[1]/div/button'
    meminput='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/input'
    memsave='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'

    #nationalities
    nationalities='//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[5]/a' #xpath
    natadd='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[1]/div/button/i'
    nationalinput='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/input'
    natsave='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'

    #corporate branding
    corporate_branding='//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[6]/a' #Xpath
    primarycolor='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div'
    primary_input='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div[2]/input[2]'
    secondarycolor='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div'
    secondary_input='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[2]/input[2]'
    primaryfontcolor='/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div'
    font_input1='/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div[2]/input[2]'
    secondaryfontcolor='/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/div/div'
    font_input2='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/div/div[2]/input[2]'
    socialcheck='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div/div/div/label/span'
    gradient1='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[5]/div/div[2]/div/div'
    gradient_input='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[5]/div/div[2]/div/div[2]/input[2]'
    gradient2='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[6]/div/div[2]/div/div'
    grad_input='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[6]/div/div[2]/div/div[2]/input[2]'
    preview='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[4]/div/button[2]'
    default='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[4]/div/button[1]'
    publish='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[4]/div/button[3]'


    #configuration
    #configuration='//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[7]/span' #Xpath
    configuration='//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[7]'
    email_config='/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[7]/ul/li[1]/a'#XPATH
    mail_input='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/input'
    mailsave='/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[5]/button[2]'
    sendmail='/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[3]/div[2]/div/label/span'
    testcheck='/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div/div/div/label/span'
    sendtest='/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[6]/div/div/div/div/label/span'
    testmail='/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[4]/div/div/div/div[2]/input'
    reset='/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[5]/button[1]'

    email_subscription='/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[7]/ul/li[2]/a' #Xpath
    leaveapplication='/html/body/div/div[1]/div[2]/div[2]/div/div/div[3]/div/div[2]/div[1]/div/div[3]/div/div/label/span'
    leaveapproval='/html/body/div/div[1]/div[2]/div[2]/div/div/div[3]/div/div[2]/div[2]/div/div[3]/div/div/label/span'
    leaveassignment='/html/body/div/div[1]/div[2]/div[2]/div/div/div[3]/div/div[2]/div[3]/div/div[3]/div/div/label/span'
    leavecancellation='/html/body/div/div[1]/div[2]/div[2]/div/div/div[3]/div/div[2]/div[4]/div/div[3]/div/div/label/span'
    leave_rejection='/html/body/div/div[1]/div[2]/div[2]/div/div/div[3]/div/div[2]/div[5]/div/div[3]/div/div/label/span'


    localization='/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[7]/ul/li[3]/a' #Xpath
    loclanguageinput='/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/div/div'
    loclanguage='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/div/div[2]/div[5]'
    dateformatinput ='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div/div/div[2]/div/div/div[1]'
    dateformat='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div/div/div[2]/div/div[2]/div[9]'
    localsave='/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/button'



    language_packages='/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[7]/ul/li[4]/a'#Xpath
    packadd='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[1]/div/button/i'
    namedrop='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div/div/div/form/div[1]/div/div[2]/div/div'
    arabic='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div/div/div/form/div[1]/div/div[2]/div/div[2]/div[24]/span'
    packsave='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div/div/div/form/div[3]/button[2]'

    config='/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[7]/span'
    modules='/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[7]/ul/li[5]/a'#Xpath
    admincheck='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/label/span'
    pimcheck='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/label/span'
    leavecheck='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/label/span'
    timecheck='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/label/span'
    recruitcheck='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[5]/div/label/span'
    performcheck='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[6]/div/label/span'
    directorycheck='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[7]/div/label/span'
    maintaincheck='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[8]/div/label/span'
    mobilecheck='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[9]/div/label/span'
    claimcheck='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[10]/div/label/span'
    modulesave='/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button'

    social_media='/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[7]/ul/li[6]/a'#Xpath
    #assert self.driver.current_url=='https://sourceforge.net/projects/orangehrm/'

    register_oauth='/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[7]/ul/li[7]/a' #Xpath
    regadd='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[1]/div/button'
    reginput='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/input'
    regurl='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/input'
    regsave='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'

    ldapconfig='/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[7]/ul/li[8]/a'#Xpath
  