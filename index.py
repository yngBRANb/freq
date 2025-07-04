#Исходные варианты текста в разном формате

input = "абвгде ёжзжг ижйжгкл абмлкадёкжн йко окппл рстжойб тгуфжнлулсх йк тбёжгцйбспч тлкйжпд ё тжгёдж зксд йкожиб тгувдёкйух нд бвйугршулу йжбвдзйдж гкспжйух у шуёбпйдц мбпбгдж сцбшу с йкоже фжнйбе нбспйбспчщ мбйжъ абмлкак"
input_split = "абвгдеёжзжгижйжгклабмлкадёкжникоокпплрстжойбтгуфжмнлулсхйктбёжгцйбспчтлкижпдётжгёджзксдйкожибтгувдёкйухндбвйугршулуйжбвдзйджгкспжйухушуёбпйдцмбпбгджсцбшусйкожефжнйбенбспйбспчщмбйжъабмлкак"
input_list = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'ж', 'г', 'и', 'ж', 'й', 'ж', 'г', 'к', 'л', 'а', 'б', 'м', 'л', 'к', 'а', 'д', 'ё', 'к', 'ж', 'н', 'и', 'к', 'о', 'о', 'к', 'п', 'п', 'л', 'р', 'с', 'т', 'ж', 'о', 'й', 'б', 'т', 'г', 'у', 'ф', 'ж', 'м', 'н', 'л', 'у', 'л', 'с', 'х', 'й', 'к', 'т', 'б', 'ё', 'ж', 'г', 'ц', 'й', 'б', 'с', 'п', 'ч', 'т', 'л', 'к', 'и', 'ж', 'п', 'д', 'ё', 'т', 'ж', 'г', 'ё', 'д', 'ж', 'з', 'к', 'с', 'д', 'й', 'к', 'о', 'ж', 'и', 'б', 'т', 'г', 'у', 'в', 'д', 'ё', 'к', 'й', 'у', 'х', 'н', 'д', 'б', 'в', 'й', 'у', 'г', 'р', 'ш', 'у', 'л', 'у', 'й', 'ж', 'б', 'в', 'д', 'з', 'й', 'д', 'ж', 'г', 'к', 'с', 'п', 'ж', 'й', 'у', 'х', 'у', 'ш', 'у', 'ё', 'б', 'п', 'й', 'д', 'ц', 'м', 'б', 'п', 'б', 'г', 'д', 'ж', 'с', 'ц', 'б', 'ш', 'у', 'с', 'й', 'к', 'о', 'ж', 'е', 'ф', 'ж', 'н', 'й', 'б', 'е', 'н', 'б', 'с', 'п', 'й', 'б', 'с', 'п', 'ч', 'щ', 'м', 'б', 'й', 'ж', 'ъ', 'а', 'б', 'м', 'л', 'к', 'а', 'к']
#известный алфавит
data_crypt = {
    "а":"д",
    "б":"о",
    "в":"б",
    "г":"р",
    "д":"ы",
    "е":"й",
    "ё":"в",
    "ж":"е",
    "з":"ч",
    "и":"г",
    "й":"н",
    "к":"а",
    "л":"л",
    "м":"к",
    "н":"м",
    "о":"ш",
    "п":"т",
    "р":"у",
    "с":"с",
    "т":"п",
    "у":"и",
    "ф":"з",
    "х":"я",
    "ц":"х",
    "ч":"ь",
    "ш":"ж",
    "щ":"ю",
    "ъ":"ц"
}
#Функция заменые символов по алфавиту
def encrypt_by_alphabet(alhpabet, text):
    for char in alhpabet.keys():
        decoded = ''.join(alhpabet.get(n, n) for n in text)
    return decoded

print(encrypt_by_alphabet(data_crypt, input))

print("\n--------------------------\n     GOOOYDA \n      SatoroGoyda\n--------------------------\n")
