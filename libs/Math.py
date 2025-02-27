#math lib for editor
vec3 = float = {3}
vec4 = float = {4}

m_MinWorldCoord = float = -64 * 1024
m_MaxWorldCoord = float = +64 * 1024

m_PassedMaxCoord = bool

def m_ExMaxCoord():
    if( m_PassedMaxCoord ):
        m_MinWorldCoord < -64 * 1024
        m_MaxWorldCoord > +64 * 1024
        
