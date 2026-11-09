#!/usr/bin/env python3
"""Generate 27 'where it sits' insets from assets/system.svg."""

import xml.etree.ElementTree as ET
import sys
from pathlib import Path
from copy import deepcopy

UNITS = {
    '01': ('Unit 01', 'P6, after verifying and merging'),
    '02': ('Unit 02', 'P2, at contract and token'),
    '03': ('Unit 03', 'P3, on worker path'),
    '04': ('Unit 04', 'P7, in master lifecycle'),
    '05': ('Unit 05', 'P7, in master lifecycle'),
    '06': ('Unit 06', 'P3, on worker path'),
    '07': ('Unit 07', 'P4, waking the master'),
    '08': ('Unit 08', 'P6, during verification'),
    '09': ('Unit 09', 'P1, one instruction'),
    '10': ('Unit 10', 'P2, at contract and token'),
    '11': ('Unit 11', 'P8, during render and upgrade'),
    '12': ('Unit 12', 'P2, at contract and token'),
    '13': ('Unit 13', 'P8, at render and upgrade'),
    '14': ('Unit 14', 'P8, at render and upgrade'),
    '15': ('Unit 15', 'P8, at render and upgrade'),
    '16': ('Unit 16', 'P7, in master lifecycle'),
    '17': ('Unit 17', 'P7, in master lifecycle'),
    '18': ('Unit 18', 'P9, writing the operations repo'),
    '19': ('Unit 19', 'P2, at contract and token'),
    '20': ('Unit 20', 'P3, on worker path'),
    '21': ('Unit 21', 'P6, after verifying and merging'),
    '22': ('Unit 22', 'P7, in master lifecycle'),
    '23': ('Unit 23', 'P7, in master lifecycle'),
    '24': ('Unit 24', 'P2, at contract and token'),
    '25': ('Unit 25', 'P8, during render and upgrade'),
    '26': ('Unit 26', 'P3, on worker path'),
    '27': ('Unit 27', 'P5, opening a pull request'),
}

CIRCLE_PATH_MAP = {
    '01': 'P6', '02': 'P2', '03': 'P3', '04': 'P7', '05': 'P7',
    '06': 'P3', '07': 'P4', '08': 'P6', '09': 'P1', '10': 'P2',
    '11': 'P8', '12': 'P2', '13': 'P8', '14': 'P8', '15': 'P8',
    '16': 'P7', '17': 'P7', '18': 'P9', '19': 'P2', '20': 'P3',
    '21': 'P6', '22': 'P7', '23': 'P7', '24': 'P2', '25': 'P8',
    '26': 'P3', '27': 'P5',
}

DIM_GREY = '#cbd5e0'

def parse_svg(path):
    tree = ET.parse(path)
    return tree

def create_inset(tree, unit_num):
    root = deepcopy(tree.getroot())
    ns = {'svg': 'http://www.w3.org/2000/svg'}
    ET.register_namespace('', 'http://www.w3.org/2000/svg')

    circle_id = f'check-{unit_num}'
    circle_elem = root.find(f".//svg:circle[@id='{circle_id}']", ns)
    if circle_elem is None:
        raise ValueError(f"Circle {circle_id} not found")

    circle_color = circle_elem.get('fill')
    target_path_id = CIRCLE_PATH_MAP.get(unit_num, '')

    # Remove only: title, legend, cue texts, color-key labels, and other disc numbers
    elements_to_remove = []
    color_key_labels = ['before dispatch', 'during', 'after, accept', 'master lifecycle', 'install']

    for text in root.findall('.//svg:text', ns):
        class_attr = text.get('class')
        text_content = ''.join(text.itertext())

        # Remove: title
        if 'the mogui harness in one picture' in text_content:
            elements_to_remove.append(text)
        # Remove: legend
        elif 'numbers are unit ids' in text_content:
            elements_to_remove.append(text)
        # Remove: cue texts
        elif class_attr == 'cue':
            elements_to_remove.append(text)
        # Remove: color-key labels (but not template box label)
        elif text_content.strip() in color_key_labels:
            elements_to_remove.append(text)
        # Remove: disc numbers of OTHER units (zero-padded match)
        elif text_content.strip().zfill(2) in [f'{i:02d}' for i in range(1, 28)]:
            if text_content.strip().zfill(2) != unit_num:
                elements_to_remove.append(text)

    for elem in elements_to_remove:
        root.remove(elem)

    # Color paths and rects
    for path in root.findall('.//svg:path', ns):
        path_id = path.get('id', '')
        if path_id == target_path_id:
            path.set('stroke', circle_color)
            # Use custom marker for highlighted path
            path.set('marker-end', f'url(#highlight-arrow-{unit_num})')
        else:
            path.set('stroke', DIM_GREY)

    for rect in root.findall('.//svg:rect', ns):
        rect.set('stroke', DIM_GREY)

    # Remove all circles except target
    for circle in root.findall('.//svg:circle', ns):
        if circle.get('id') != circle_id:
            root.remove(circle)

    # Enhance target circle
    circle_elem.set('r', '26')
    circle_elem.set('stroke-width', '2')
    circle_elem.set('stroke', circle_color)
    circle_elem.set('fill-opacity', '0.95')
    circle_elem.set('filter', f'url(#glow-{unit_num})')

    # Update marker fill to dim grey
    defs = root.find('./svg:defs', ns)
    if defs is not None:
        for marker in defs.findall('./svg:marker', ns):
            for path_elem in marker.findall('./svg:path', ns):
                path_elem.set('fill', DIM_GREY)

    # Create defs if needed
    if defs is None:
        defs = ET.Element('{http://www.w3.org/2000/svg}defs')
        root.insert(0, defs)

    # Remove old filters
    for filt in list(defs.findall('./svg:filter', ns)):
        if 'glow' in filt.get('id', ''):
            defs.remove(filt)

    # Add highlight arrow marker
    marker = ET.Element('{http://www.w3.org/2000/svg}marker')
    marker.set('id', f'highlight-arrow-{unit_num}')
    marker.set('markerWidth', '10')
    marker.set('markerHeight', '10')
    marker.set('refX', '8')
    marker.set('refY', '5')
    marker.set('orient', 'auto')
    arrow_path = ET.Element('{http://www.w3.org/2000/svg}path')
    arrow_path.set('d', 'M0,0 L10,5 L0,10 z')
    arrow_path.set('fill', circle_color)
    marker.append(arrow_path)
    defs.append(marker)

    # Create glow filter with crisp disc
    glow_filter = ET.Element('{http://www.w3.org/2000/svg}filter')
    glow_filter.set('id', f'glow-{unit_num}')
    glow_filter.set('x', '-50%')
    glow_filter.set('y', '-50%')
    glow_filter.set('width', '200%')
    glow_filter.set('height', '200%')

    blur = ET.Element('{http://www.w3.org/2000/svg}feGaussianBlur')
    blur.set('in', 'SourceGraphic')
    blur.set('stdDeviation', '5')
    blur.set('result', 'coloredBlur')
    glow_filter.append(blur)

    fmerge = ET.Element('{http://www.w3.org/2000/svg}feMerge')
    node1 = ET.Element('{http://www.w3.org/2000/svg}feMergeNode')
    node1.set('in', 'coloredBlur')
    node2 = ET.Element('{http://www.w3.org/2000/svg}feMergeNode')
    node2.set('in', 'SourceGraphic')
    fmerge.append(node1)
    fmerge.append(node2)
    glow_filter.append(fmerge)
    defs.append(glow_filter)

    # Add title
    title = ET.Element('{http://www.w3.org/2000/svg}title')
    unit_name, place = UNITS[unit_num]
    title.text = f'{unit_name}: {place}'
    root.insert(0, title)

    return ET.ElementTree(root)

def main():
    svg_path = Path(__file__).parent.parent / 'system.svg'
    output_dir = Path(__file__).parent if len(sys.argv) < 2 else Path(sys.argv[1])

    if not svg_path.exists():
        print(f'Error: {svg_path} not found', file=sys.stderr)
        sys.exit(1)

    output_dir.mkdir(parents=True, exist_ok=True)
    tree = parse_svg(svg_path)

    for unit_num in range(1, 28):
        unit_str = f'{unit_num:02d}'
        try:
            inset_tree = create_inset(tree, unit_str)
            output_path = output_dir / f'{unit_str}-where.svg'
            inset_tree.write(str(output_path), encoding='utf-8', xml_declaration=True)
        except Exception as e:
            print(f'Error generating {unit_str}-where.svg: {e}', file=sys.stderr)
            import traceback
            traceback.print_exc()
            sys.exit(1)

if __name__ == '__main__':
    main()
