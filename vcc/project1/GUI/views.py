from django.shortcuts import render
import sys
import libvirt

def index(request):
    test = ""
    try:
        conn = libvirt.open('qemu:///system')

        if conn == None:
            test = 'Failed to open connection to qemu:///system' + str(file=sys.stderr)
        else:
            test = 'good'+' Connection is Alive: '+str(conn.isAlive())

    except:
        test = "dont have permissions"
        
    return render(request, 'GUI/home.html',{'test':test})

def createdby(request):
    return render(request, 'GUI/createdby.html')