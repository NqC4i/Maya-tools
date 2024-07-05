import math
def display_vertex_distances():
    # 選択されたオブジェクトの頂点を取得
    selected_objects = cmds.ls(selection=True)
    if not selected_objects:
        cmds.warning("オブジェクトが選択されていません。")
        return

    # 頂点の座標を取得
    vertices = cmds.ls(selected_objects, flatten=True)
    vertex_positions = [cmds.pointPosition(v) for v in vertices]
    if len( vertex_positions ) != 2:
        cmds.warning("二個の頂点を選択してください")
        return
    
    p0 = vertex_positions[0]
    p1 = vertex_positions[1]
    
    rr = (p0[0] - p1[0])**2 +(p0[1] -p1[1])**2+(p0[2]-p1[2])**2 
    r = math.sqrt(rr)
    cmds.confirmDialog(title="頂点距離情報", message=r)
    
display_vertex_distances()
