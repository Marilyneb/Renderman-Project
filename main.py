import prman

ri = prman.Ri()

filename = "avocado.rib"
ri.Begin(filename)
ri.Hider("raytrace", {"int incremental": [1]})

ri.Integrator("PxrPathTracer", "integrator", {"int numLightSamples": [16], "int numBxdfSamples": [16]})

ri.Hider("raytrace", {
        "int incremental": [1],
        "int minsamples": 128,
        "int maxsamples": 256
})

ri.Display("Avocado.tif", "file", "rgba")
ri.Format(1920, 1080, 1) 
# Camera settings
ri.Projection("perspective", {"fov": 25}) 

ri.Scale(0.01, 0.01, 0.01)
ri.Translate(0, -1, 12)
ri.Rotate(-20, 1, 0, 0)
# World description
ri.WorldBegin()
ri.AttributeBegin()
ri.Pattern("PxrTexture", "ground_texture_pattern", {
        "string filename": "wood2.tx",
    })
ri.Bxdf("PxrDisney", "ground_shader", {
        "reference color baseColor": ["ground_texture_pattern:resultRGB"]
    })

ri.TransformBegin()
ri.Rotate(-90, 1, 0, 0)
ri.Scale(80, 80,80)  #
ri.Patch("bilinear", {"P": [-1, -1, 0, 1, -1, 0, -1, 1, 0, 1, 1, 0]})
ri.TransformEnd()
ri.AttributeEnd()

# HDRI environment map 
ri.TransformBegin()
ri.Rotate(-20,0,1,0)
ri.Light("PxrDomeLight", "dome_light", {"string lightColorMap": "hdri.tx", "float intensity": 0.75})
ri.TransformEnd()

  # rectangular light 
ri.TransformBegin()
ri.Translate(-2, 10, 0) 
ri.Scale(5, 5, 5)  
ri.Rotate(20, 1, 0, 0)  
ri.Rotate(70, 0, 1, 0)  
ri.Light("PxrRectLight", "spotlight", {
        "float intensity": 3.5,  
        "color lightColor": [1, 1, 1],  
        "int enableShadows": 1,  
        "color shadowColor": [0, 0, 0],  

})
ri.TransformEnd()

ri.Attribute("displacementbound", {"float sphere": [8.0]})

# Displacement pattern for the avocado 
ri.Pattern("avocado_displacement", "avocado_displacement_pattern", {"float scale": 1, "float frequency": 30.0, "float amplitude": 0.05})
ri.Displace("PxrDisplace", "avocado_displacement", {"reference float dispScalar": ["avocado_displacement_pattern:resultF"]})

# avocado_texture pattern
ri.Pattern("avocado_texture", "avocado_texture_pattern", {"float noise_scale": 0.1, "string color_texture": "Avocado_COLOR.tx", "string spec_texture": "Avocado_SPEC.tx", "string norm_texture": "Avocado_NORM.tx"})

#parameters for the avocado_surface_shader
ri.Bxdf("PxrDisney", "avocado_surface_shader", {
    "reference color baseColor": ["avocado_texture_pattern:resultRGB"],
    "float roughness": 0.4,
    "float specular": 0.4,
    "float clearcoat": 0.1,
    "float clearcoatGloss": 0.05
})

# Add avocado geometry 
ri.TransformBegin()
ri.Translate(0, 1.64, 0)
ri.Scale(1.4, 1.0, 1.0)
ri.Rotate(-20, 1, 0, 10)
ri.Sphere(1, -1, 1, 360)
ri.TransformEnd()

# Add stem to the avocado 
ri.TransformBegin()
ri.Translate(1.5, 1.66, 0)
ri.Rotate(90, 0, 1, 0)
ri.Rotate(20, 0, 0, 1)
ri.Scale(0.05, 0.05, 0.15)
ri.Bxdf("PxrDisney", "stem_shader", {"color baseColor": [0.2, 0.1, 0.05]})
ri.Cylinder(1, -1, 1, 360)
ri.TransformEnd()


ri.WorldEnd()

ri.End()
