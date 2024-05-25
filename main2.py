import prman

def draw_avocado(ri, position, scale, rotation):
    # Define the displacement pattern for the avocado 
    ri.Pattern("avocado_displacement", "avocado_displacement_pattern", {
        "float scale": 1, 
        "float frequency": 30.0, 
        "float amplitude": 0.05
    })
    ri.Displace("PxrDisplace", "avocado_displacement", {
        "reference float dispScalar": ["avocado_displacement_pattern:resultF"]
    })

    # Add avocado geometry 
    ri.TransformBegin()
    ri.Translate(position[0], position[1], position[2])
    ri.Scale(scale[0], scale[1], scale[2])
    ri.Rotate(rotation[0], rotation[1], rotation[2], rotation[3])
    ri.Sphere(1, -1, 1, 360)

    # Add stem to the avocado 
    ri.TransformBegin()
    ri.Translate(0.82, 0.6, -0.1)
    ri.Rotate(50, 0, 1, 0)
    ri.Rotate(20, 0, 0, 1)
    ri.Scale(0.07, 0.07, 0.2)
    ri.Bxdf("PxrDisney", "stem_shader", {"color baseColor": [0.2, 0.1, 0.05]})
    ri.Cylinder(1, -1, 1, 360)
    ri.TransformEnd()
    ri.TransformEnd()

def main():
    ri = prman.Ri()
    filename = "avocado_scene.rib"
    ri.Begin(filename)


    ri.Hider("raytrace", {"int incremental": [1]})
    ri.Integrator("PxrPathTracer", "integrator", {"int numLightSamples": [16], "int numBxdfSamples": [16]})
    ri.Hider("raytrace", {
        "int incremental": [1],
        "int minsamples": 128,
        "int maxsamples": 256
    })

    # Display settings
    ri.Display("avocados.tif", "file", "rgba")
    ri.Format(1920, 1080, 1)  

    # Camera settings
    ri.Projection("perspective", {"fov": 35})  
    ri.Scale(0.01, 0.01, 0.01)
    ri.Translate(-0.7, 0, 11)
    ri.Rotate(-20, 1, 0, 0)
     #ri.DepthOfField(15.0, 0.01, 2.0)

    # World description
    ri.WorldBegin()

    ri.AttributeBegin()

    ri.Pattern("PxrTexture", "ground_texture_pattern", {
        "string filename": "wood2.tx",
    })
    
    ri.Bxdf("PxrDisney", "ground_shader", {
        "reference color baseColor": ["ground_texture_pattern:resultRGB"]
    })

    # Table 
    ri.TransformBegin()
    ri.Rotate(-90, 1, 0, 0)
    ri.Scale(80, 80,80)  
    ri.Patch("bilinear", {"P": [-1, -1, 0, 1, -1, 0, -1, 1, 0, 1, 1, 0]})
    ri.TransformEnd()
    ri.AttributeEnd()

    #  HDRI environment map 
    ri.TransformBegin()
    ri.Rotate(-20,0,1,0)
    ri.Light("PxrDomeLight", "dome_light", {"string lightColorMap": "hdri.tx", "float intensity": 0.75})
    ri.TransformEnd()

    # rectangular light 
    ri.TransformBegin()
    ri.Translate(-3, 10, 0) 
    ri.Scale(5, 5, 5)  
    ri.Rotate(20, 1, 0, 0)  
    ri.Rotate(70, 0, 1, 0)  
    ri.Light("PxrRectLight", "spotlight", {
        "float intensity": 5.5,  
        "color lightColor": [1, 1, 1],  
        "int enableShadows": 1,  
        "color shadowColor": [0, 0, 0],  

    })
    ri.TransformEnd()


    ri.Attribute("displacementbound", {"float sphere": [8.0]})
    # Draw the avocado 1
    ri.TransformBegin()
    ri.Pattern("avocado_texture", "avocado_texture_pattern_1", {
        "float noise_scale": 0.1, 
        "string color_texture": "Avocado_COLOR.tx", 
        "string spec_texture": "Avocado_SPEC.tx", 
        "string norm_texture": "Avocado_NORM.tx"
    })
    ri.Bxdf("PxrDisney", "avocado_surface_shader_1", {
        "reference color baseColor": ["avocado_texture_pattern_1:resultRGB"],
        "float roughness": 0.4,
        "float specular": 0.5,
        "float clearcoat": 0.1,
        "float clearcoatGloss": 0.05
    })
    draw_avocado(ri, [-2, 1.64, 0], [1.4, 1.0, 1.0], [-20, 1, 1, 1])
    ri.TransformEnd()

    # Draw the avocado 2
    ri.TransformBegin()
    ri.Pattern("avocado_texture2", "avocado_texture_pattern_2", {
        "float noise_scale": 0.1, 
        "string color_texture": "Avocado_COLOR.tx", 
        "string spec_texture": "Avocado_SPEC.tx", 
        "string norm_texture": "Avocado_NORM.tx"
    })
    ri.Bxdf("PxrDisney", "avocado_surface_shader_2", {
        "reference color baseColor": ["avocado_texture_pattern_2:resultRGB"],
        "float roughness": 0.4,
        "float specular": 0.5,
        "float clearcoat": 0.1,
        "float clearcoatGloss": 0.05
    })
    draw_avocado(ri, [4, 1.3, -2], [1.1, 0.9, 0.9], [-30, 0, 1, 45])  
    ri.TransformEnd()

    # Draw the avocado 3
    ri.TransformBegin()
    ri.Pattern("avocado_texture1", "avocado_texture_pattern_3", {
        "float noise_scale": 0.1, 
        "string color_texture": "Avocado_COLOR.tx", 
        "string spec_texture": "Avocado_SPEC.tx", 
        "string norm_texture": "Avocado_NORM.tx"
    })
    ri.Bxdf("PxrDisney", "avocado_surface_shader_3", {
        "reference color baseColor": ["avocado_texture_pattern_3:resultRGB"],
        "float roughness": 0.4,
        "float specular": 0.5,
        "float clearcoat": 0.1,
        "float clearcoatGloss": 0.05
    })
    draw_avocado(ri, [3, 1.64, 4], [1.3, 1.0, 1.0], [-180, 1, 1, 1])  
    ri.TransformEnd()

    # Draw the avocado 4
    ri.TransformBegin()
    ri.Pattern("avocado_texture", "avocado_texture_pattern_4", {
        "float noise_scale": 0.1, 
        "string color_texture": "Avocado_COLOR.tx", 
        "string spec_texture": "Avocado_SPEC.tx", 
        "string norm_texture": "Avocado_NORM.tx"
    })
    ri.Bxdf("PxrDisney", "avocado_surface_shader_4", {
        "reference color baseColor": ["avocado_texture_pattern_4:resultRGB"],
        "float roughness": 0.4,
        "float specular": 0.4,
        "float clearcoat": 0.1,
        "float clearcoatGloss": 0.05
    })
    draw_avocado(ri, [-0.5, 1.0, -5], [0.8, 0.6, 0.6], [200, 0, 1, 0])  
    ri.TransformEnd()    

    # Draw the avocado 5
    ri.TransformBegin()
    ri.Pattern("avocado_texture1", "avocado_texture_pattern_5", {
        "float noise_scale": 0.1, 
        "string color_texture": "Avocado_COLOR.tx", 
        "string spec_texture": "Avocado_SPEC.tx", 
        "string norm_texture": "Avocado_NORM.tx"
    })
    ri.Bxdf("PxrDisney", "avocado_surface_shader_5", {
        "reference color baseColor": ["avocado_texture_pattern_5:resultRGB"],
        "float roughness": 0.4,
        "float specular": 0.4,
        "float clearcoat": 0.1,
        "float clearcoatGloss": 0.05
    })
    draw_avocado(ri, [10, 1.3, 9], [1.4, 1.0, 1.0], [-60, 1, 0, 1])
    ri.TransformEnd()

    # Draw the avocado 6
    ri.TransformBegin()
    ri.Pattern("avocado_texture1", "avocado_texture_pattern_6", {
        "float noise_scale": 0.1, 
        "string color_texture": "Avocado_COLOR.tx", 
        "string spec_texture": "Avocado_SPEC.tx", 
        "string norm_texture": "Avocado_NORM.tx"
    })
    ri.Bxdf("PxrDisney", "avocado_surface_shader_6", {
        "reference color baseColor": ["avocado_texture_pattern_6:resultRGB"],
        "float roughness": 0.4,
        "float specular": 0.4,
        "float clearcoat": 0.1,
        "float clearcoatGloss": 0.05
    })
    draw_avocado(ri, [-1, 1.8, 12], [1.3, 1.0, 1.0], [-220, 1, 1, 1])  
    ri.TransformEnd()

    ri.WorldEnd()
    ri.End()

if __name__ == "__main__":
    main()
