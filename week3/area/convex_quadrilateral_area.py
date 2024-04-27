'''Homework'''
def four_lines_area(k_1, c_1, k_2, c_2, k_3, c_3, k_4, c_4):
    if (k_1 == k_2 and k_2 == k_3) or (k_1 == k_2 and k_2 == k_4):
        return 0
    if (k_1 == k_3 and k_3 == k_4) or (k_2 == k_3 and k_3 == k_4):
        return 0
    pnt_1 = lines_intersection(k_1, c_1, k_2, c_2)
    pnt_2 = lines_intersection(k_2, c_2, k_3, c_3)
    pnt_3 = lines_intersection(k_3, c_3, k_4, c_4)
    pnt_4 = lines_intersection(k_4, c_4, k_1, c_1)
    if pnt_1 is None or pnt_2 is None or pnt_3 is None or pnt_4 is None:
        return 0
    a_side = distance(pnt_1[0], pnt_1[1], pnt_2[0], pnt_2[1])
    b_side = distance(pnt_2[0], pnt_2[1], pnt_3[0], pnt_3[1])
    c_side = distance(pnt_3[0], pnt_3[1], pnt_4[0], pnt_4[1])
    d_side = distance(pnt_4[0], pnt_4[1], pnt_1[0], pnt_1[1])
    f1_diagonal = distance(pnt_1[0], pnt_1[1], pnt_3[0], pnt_3[1])
    f2_diagonal = distance(pnt_2[0], pnt_2[1], pnt_4[0], pnt_4[1])
    area = quadrangle_area(a_side, b_side, c_side, d_side, f1_diagonal, f2_diagonal)

    return 0


def lines_intersection(k_1:float, c_1:float, k_2:float, c_2:float)->list:
    if k_1!=k_2:
        x_1 = (c_2 - c_1)/(k_1 - k_2)
        y_1 = k_1*x_1 + c_1
        return (round(x_1,2), round(y_1,2))
    return None

def distance(x_1:float, y_1:float, x_2:float, y_2:float)->float:
    distance_ = (((x_2-x_1)**2)+((y_2-y_1)**2))**(1/2)
    return round(distance_,2)


def quadrangle_area(a_1:float, b_1:float, c_1:float, d_1:float, f_1:float, f_2:float)->float:
    if (f_1<b_1+a_1 and
        b_1<f_1+a_1 and
        a_1<f_1+b_1):
        if (f_1<d_1+c_1 and
        d_1<f_1+c_1 and
        c_1<f_1+d_1):
            area = ((4*(f_1**2)*(f_2**2) - ((b_1**2)+(d_1**2)-(a_1**2)-(c_1**2))**2)/16)**(1/2)
            return round(area,2)
    return None
