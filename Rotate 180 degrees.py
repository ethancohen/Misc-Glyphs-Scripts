#MenuTitle: Rotate 180 degrees
# -*- coding: utf-8 -*-
__doc__="""
Rotate 180 degrees
"""

import math
import GlyphsApp

f = Glyphs.font
l = Font.selectedLayers[0]
g = l.parent
selection = l.selection

# rotate nodes around center
def rotate(ymin, ymax, enforceSelection):
	if g.name.split(".")[0] in "bdfhjklpqy":
		yCenter = l.master.xHeight / 2
	else:
		yCenter = ymax - ((ymax - ymin) / 2)
	xCenter = l.width * 0.5
	Transform = NSAffineTransform.transform()
	Transform.translateXBy_yBy_(xCenter, yCenter)
	Transform.rotateByDegrees_(180)
	Transform.translateXBy_yBy_(-xCenter, -yCenter)
	for Path in Layer.paths:
	    for Node in Path.nodes:
	    	if Node.selected == True or enforceSelection == False:
		        Node.position = Transform.transformPoint_(NSMakePoint(Node.x, Node.y))

# change rotation attribute of components
def rotateComponent(enforceSelection):
	for Component in Layer.components:
		if Component.selected == True or enforceSelection == False:
			if Component.rotation == 0:
				Component.rotation = 180
			else:
				Component.rotation = 0

# get ymin and ymax from all nodes in selection and use them to rotate selection
def stuffSelected():
	ymax = max(node.y for node in selection)
	ymin = min(node.y for node in selection)
	rotate(ymin,ymax,enforceSelection=True)
	

# get ymin and ymax from all nodes in layer and use them to rotate everything
def nothingSelected():
	nodes = []
	for path in l.paths:
		for node in path.nodes:
			nodes.append(node.y)
	if len(nodes) > 0:
		ymax = max(nodes)
		ymin = min(nodes)
		rotate(ymin,ymax,enforceSelection=False)

# if 3 or more things are selected, rotate selection; otherwise rotate everything
if selection:
	if len(selection) < 5:
		l.clearSelection()
		nothingSelected()
		rotateComponent(enforceSelection=False)
	else:
		stuffSelected()
		rotateComponent(enforceSelection=True)

# if nothing is selected, rotate everything
else:
	if l.paths:
		nothingSelected()
	rotateComponent(enforceSelection=False)