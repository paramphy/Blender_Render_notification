import bpy



class LayoutDemoPanel(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "Email Recipient Detail"
    bl_idname = "SCENE_PT_layout"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene"

    def draw(self, context):
        layout = self.layout

        scene = context.scene
        
        col = self.layout.column(align = True)
        col.prop(context.scene, "email")
        
        col = self.layout.column(align = True)
        col.prop(context.scene, "password")
        
       

        # Different sizes in a row
        layout.label(text="Different button sizes:")
        row = layout.row(align=True)
        row.operator("render.render")

        sub = row.row()
        sub.scale_x = 2.0
        sub.operator("render.render")

        row.operator("render.render")
        
        
        


def register():
    bpy.utils.register_class(LayoutDemoPanel)
    bpy.types.Scene.email = bpy.props.StringProperty \
        (
            name = "Email ID",
            description = "Email id of the recipient",
            default = "abc@gmail.com"
        )
    bpy.types.Scene.password = bpy.props.StringProperty \
        (
            name = "Password",
            description = "Generated password",
            default = ""
        )
    
    


def unregister():
    bpy.utils.unregister_class(LayoutDemoPanel)
    del bpy.types.Scene.my_string_prop
    


if __name__ == "__main__":
    register()
