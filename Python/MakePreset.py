#!/usr/local/bin/python

import collections
import json
import os.path
import sys
import xml.dom.minidom

import defaults

def SetNodeValue(node, kwds):
  for k, v in kwds.iteritems():
    node.setAttribute(k, v)

def CreateDocument(tag, attributes):
  impl = xml.dom.minidom.getDOMImplementation()
  document = impl.createDocument(None, tag, None)
  SetNodeValue(document.documentElement, attributes)
  return document

def CreateElement(document, parent, tag, attributes={}):
  element = document.createElement(tag)
  SetNodeValue(element, attributes)
  parent.appendChild(element)
  return element

def Print(document, output):
  output.write(document.toprettyxml(indent='  '))

def Add(document, names, data, tag, parent, nameField):
  sub = data[tag]
  for name in names:
    d = sub.get(name, {})
    d = collections.OrderedDict((str(k), v) for k, v in d.iteritems())
    attributes = defaults.Get(tag, {nameField:name}, d)
    CreateElement(document, parent, tag, attributes)

def MakePreset(data, output):
  d = defaults.Get('DbAudiowarePreset', dict(name=data['name']), {})
  document = CreateDocument('DbAudiowarePreset', d)
  root = document.documentElement
  params = CreateElement(document, root, 'Params')
  dmx = CreateElement(document, root, 'DmxUniverse')

  Add(document, defaults.PARAM_NAMES, data, 'Param', params, 'nm')
  Add(document, defaults.DMX_NAMES, data, 'c', dmx, 'n')

  Print(root, output)

if __name__ == '__main__':
  if len(sys.argv) is 2:
    with open(sys.argv[1]) as input:
      data = json.load(input)
      with open('sample.xml', 'w') as output:
        MakePreset(data, output)

  else:
    print 'Usage: %s json-filename' % sys.argv[0]
    sys.exit(-1)
