
bl_info = {
    "name": "Render Notification",
    "author": "Param",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "Global",
    "description": "Displays a system notification when render is complete on Linux and Windows based systems",
    "warning": "",
    "wiki_url": "",
    "category": "System",
    }
    
    
import bpy, os, locale, subprocess
from bpy.app.handlers import persistent
import smtplib
import time
t = time.time()


#Function to install plyer Librery
def install_pip_dep(module_name):
    python_path = bpy.app.binary_path_python
    subp = subprocess.run([python_path, "-m", "ensurepip","--user"])
    if subp.returncode != 0:
        return False
    subp = subprocess.run([python_path, "-m", "pip", "install", module_name,"--user"])
    if subp.returncode != 0:
        return False
    return True    

#if __name__ == '__main__':
    
    #install_pip_dep("plyer")
    
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('parametricblending@gmail.com', 'jcpssizkgljywcgc')

    subject = 'Render Status'
    body = 'Your render is complete.'
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'parametricblending@gmail.com',
        'parameshchandra28@gmail.com',
         msg
        )
    print('Render completion report sent ')

    server.quit()


from plyer import notification
loc = locale.getlocale() # get current locale
locx = loc[:3]
locale.getdefaultlocale()


        
@persistent
def is_render_complete(scene):

        
#WINDOWS
        
        if os.name=='nt' and locx=="es_":#Español
            notification.notify(
            message='Render Finalizado',
            app_name= 'Blender',
            #app_icon = cd + 'blender_icon_32x32.ico'
            )
        elif os.name=='nt' and locx=="ca_":#Catalán
            notification.notify(
            message='S´ha finalitzat la prestació!',
            app_name= 'Blender',
            
            )
            
        elif os.name=='nt' and locx=="fr_":#Frances
            notification.notify(
            message='Rendu terminé',
            app_name= 'Blender',
            
            )
            
        elif os.name=='nt' and locx=="it_":#Italiano
            notification.notify(
            message='Rendering finito',
            app_name= 'Blender',
            
            )
            
        elif os.name=='nt' and locx=="pt_":#Protugues
            notification.notify(
            message='Renderizado concluído!',
            app_name= 'Blender',
            
            )
           
        elif os.name=='nt' and locx=="de_":#Alemán
            notification.notify(
            message='Fertig machen!',
            app_name= 'Blender',
            
            )
            
        else:
            notification.notify(
            message='Render Finished!',
            app_name= 'Blender',
            #app_icon = 'blender_icon_32x32.ico'
            
            )
            
        #send_mail()
        
def render_time(scene):
        print ("Seconds elapsed since the epoch are : ",end="") 
        print(time.time()-t) 
    
        #bpy.app.handlers.frame_change_post.append(render_time)       
            

classes = ()
register, unregister = bpy.utils.register_classes_factory(classes)

def register():
    
    bpy.app.handlers.render_complete.append(is_render_complete)
   
     
def unregister():
   
    bpy.app.handlers.render_complete.remove(is_render_complete)
    
     

if __name__ == '__main__':
    
    register()
    
    
