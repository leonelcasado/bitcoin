# coding: utf-8
from __future__ import unicode_literals

import os
import re
from django import template
from collections import OrderedDict
from django.template import Library, Node, VariableDoesNotExist
from django.core.validators import RegexValidator
from django.contrib import messages
from django.core.exceptions import ValidationError
from PIL import ImageFile
from django.core.mail import send_mail
from django.contrib.auth.models import Group
from bitcoin.settings import EMAIL_HOST_USER
from urllib.parse import urlencode
#=========================================================
register = Library()
#=========================================================
ValidarAlfanumerico = RegexValidator(r'^[0-9a-zA-Z]*$','Este campo não aceita caracteres especiais.')
ValidarNumero= RegexValidator(r'^[0-9]*$','Este campo só aceita valores numéricos.')
ValidarNumeroMascarado= RegexValidator(r'^[0-9./-]*$','Este campo só aceita valores numéricos.')
#=========================================================
MSG_SUCCESS=u'Serviço executado com sucesso!'
MSG_NOT_FOUND=u'Nenhum registro encontrado!'
MSG_FORBIDDEN=u'Serviço sem permissão!'
MSG_FAILURE=u'Erro ao executado o serviço!'
#=========================================================
MSG_ADD=u'Registro cadastrado com sucesso!'
MSG_EDIT=u'Registro alterado com sucesso!'
MSG_DEL=u'Registro excluído com sucesso!'
MSG_RESET_PASSWORD=u'Senha resetada com sucesso!'
#=========================================================
MSG_PROTECTION_ADD=u'Inclusão não permitida!'
MSG_PROTECTION_EDIT=u'Alteração não permitida!'
MSG_PROTECTION_DEL=u'Exclusão não permitida!'
MSG_INTEGRITY_ERROR=u'Registro duplicado!'
#=========================================================
def limpar_messages(request):
    storage = messages.get_messages(request)
    storage.used = True
#=========================================================
@register.filter('get_nome_mes')
def get_nome_mes(value):
    mes=['JANEIRO','FEVEREIRO','MARÇO','ABRIL','MAIO','JUNHO','JULHO','AGOSTO','SETEMBRO','OUTUBRO','NOVEMBRO','DEZEMBRO']
    return '%s' % mes[value-1]
    #return calendar.month_name[value]
#=========================================================
#@register.filter('get_value_from_dict')
@register.simple_tag
def get_value_from_dict(dict_data, key):
    """
    usage example {{ dict_data|get_value_from_dict:key }}
    usage example {% get_value_from_dict dict_data key %}
    """
    if key!=None:
        #dict_data.__getitem__(key)[1] # Só de key for int 
        for obj in dict_data: 
            if str(key) == str(obj[0]): 
                return obj[1]
    return key
#=========================================================
@register.filter('mascarar_cpf')
def mascarar_cpf(valor):
    if valor:
        if (len(valor)==11):
            return '{}{}{}.{}{}{}.{}{}{}-{}{}'.format(*valor)

        elif (len(valor)==10):
            return '{}{}{}.{}{}{}.{}{}{}-{}{}'.format(*'0'+valor)

        else:
            return valor        

    else:
        return valor        
#=========================================================
@register.filter('mascarar_cnpj')
def mascarar_cnpj(valor):
    if valor:
        if (len(valor)==14):
            return '{}{}.{}{}{}.{}{}{}/{}{}{}{}-{}{}'.format(*valor)

        else:
            return valor        

    else:
        return valor        
#=========================================================
@register.filter('mascarar_telefone')
def mascarar_telefone(valor):
    if valor:
        if (len(valor)==8):
            return '{}{}{}{}-{}{}{}{}'.format(*valor)
        
        elif (len(valor)==9):
            return '{}-{}{}{}{}-{}{}{}{}'.format(*valor)
    
        elif (len(valor)==10):
            return '({}{}){}{}{}{}-{}{}{}{}'.format(*valor)
    
        elif (len(valor)==11):
            return '({}{}){}-{}{}{}{}-{}{}{}{}'.format(*valor)
        
        else:
            return valor
        
    else:
        return valor
#=========================================================
@register.filter('converter_data_numero')
def converter_data_numero(valor):
    if valor:
        if (len(valor)==5):
            data_numerica= ''.join((c for c in valor if 48 <= ord(c) <= 57))
            #print data_numerica
            dia=data_numerica[0:2]
            #print dia
            mes=data_numerica[2:4]
            #print mes+''+dia
            return mes+''+dia

        elif (len(valor)==10):
            data_numerica= ''.join((c for c in valor if 48 <= ord(c) <= 57))
            #print data_numerica
            dia=data_numerica[0:2]
            #print dia
            mes=data_numerica[2:4]
            #print mes
            ano=data_numerica[4:8]
            #print ano
            #print ano+''+mes+''+dia
            return ano+''+mes+''+dia

        elif (len(valor)>=19):
            data_numerica= ''.join((c for c in valor if 48 <= ord(c) <= 57))
            #print data_numerica
            dia=data_numerica[0:2]
            #print dia
            mes=data_numerica[2:4]
            #print mes
            ano=data_numerica[4:8]
            #print ano
            hora=data_numerica[8:10]
            minuto=data_numerica[10:12]
            segundo=data_numerica[12:14]
            #print ano+''+mes+''+dia+''+hora+''+minuto+''+segundo
            return ano+''+mes+''+dia+''+hora+''+minuto+''+segundo
        
        else:
            return valor        

    else:
        return valor 
#=========================================================
@register.filter('converter_data_numero_db')
def converter_data_numero_db(valor):
    if valor:
        if (len(valor)==5):
            data_numerica= ''.join((c for c in valor if 48 <= ord(c) <= 57))
            #print data_numerica
            dia=data_numerica[0:2]
            #print dia
            mes=data_numerica[2:4]
            #print mes+'-'+dia
            return mes+'-'+dia
        
        elif (len(valor)==8):
            data_numerica= ''.join((c for c in valor if 48 <= ord(c) <= 57))
            #print data_numerica
            dia=data_numerica[0:2]
            #print dia
            mes=data_numerica[2:4]
            #print mes
            ano=data_numerica[4:8]
            #print ano
            #print ano+'-'+mes+'-'+dia
            return ano+'-'+mes+'-'+dia

        elif (len(valor)==10):
            data_numerica= ''.join((c for c in valor if 48 <= ord(c) <= 57))
            #print data_numerica
            dia=data_numerica[0:2]
            #print dia
            mes=data_numerica[2:4]
            #print mes
            ano=data_numerica[4:8]
            #print ano
            #print ano+'-'+mes+'-'+dia
            return ano+'-'+mes+'-'+dia
        
        elif (len(valor)>=19):
            data_numerica= ''.join((c for c in valor if 48 <= ord(c) <= 57))
            #print data_numerica
            dia=data_numerica[0:2]
            #print dia
            mes=data_numerica[2:4]
            #print mes
            ano=data_numerica[4:8]
            #print ano
            hora=data_numerica[8:10]
            minuto=data_numerica[10:12]
            segundo=data_numerica[12:14]
            #print ano+'-'+mes+'-'+dia+' '+hora+':'+minuto+':'+segundo
            return ano+'-'+mes+'-'+dia+' '+hora+':'+minuto+':'+segundo

        else:
            return valor        

    else:
        return valor 
#=========================================================
@register.filter('converter_hora_numero_db')
def converter_hora_numero_db(valor):
    if valor:
        if (len(valor)==4):
            hora_numerica= ''.join((c for c in valor if 48 <= ord(c) <= 57))
            #print hora_numerica
            hora=hora_numerica[0:2]
            #print hora
            minuto=hora_numerica[2:4]
            #print hora+':'+minuto
            return hora+':'+minuto

        if (len(valor)>=6):
            hora_numerica= ''.join((c for c in valor if 48 <= ord(c) <= 57))
            #print hora_numerica
            hora=hora_numerica[0:2]
            #print hora
            minuto=hora_numerica[2:4]
            #print hora+':'+minuto
            segundo=hora_numerica[4:]
            #print hora+':'+minuto+':'+segundo
            return hora+':'+minuto+':'+segundo
        
        else:
            return valor        

    else:
        return valor 
#=========================================================
def validate_file_extension_pdf(value):
    ext = os.path.splitext(value.name)[1]  # [0] Retorna caminho+nome do arquivo
    valid_extensions = ['.pdf']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Inserir apenas arquivos em PDF.')
#=========================================================
def validate_file_extension_img(value):
    ext = os.path.splitext(value.name)[1]  # [0] Retorna caminho+nome do arquivo
    valid_extensions = ['.jpg','.png','.jpeg','.gif']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Inserir apenas arquivos com extensão:JPG,PNG,JPEG,GIF')
#=========================================================
#https://github.com/alexei/django-template-extensions
class IifNode(template.Node):
    def __init__(self, exp1 = None, exp2 = None, exp3 = None):
        if not exp3:
            exp3 = exp2
            exp2 = exp1
        self.exp1 = self.fix_type(exp1)
        self.exp2 = self.fix_type(exp2)
        self.exp3 = self.fix_type(exp3)

    def render(self, context):
        try:
            if isinstance(self.exp1, template.Variable):
                self.exp1 = self.exp1.resolve(context)
            if isinstance(self.exp2, template.Variable):
                self.exp2 = self.exp2.resolve(context)
            if isinstance(self.exp3, template.Variable):
                self.exp3 = self.exp3.resolve(context)
            return self.exp2 if bool(self.exp1) else self.exp3
        except template.VariableDoesNotExist:
            return ""

    def fix_type(self, v):
        try:
            i = int(v)
            if str(i) == v:
                v = i
            else:
                raise ValueError()
        except ValueError:
            try:
                f = float(v)
                v = f
            except ValueError:
                if v[0] == v[-1] and v[0] in ('"', "'"):
                    v = v[1:-1]
                elif v == "None":
                    v = None
                elif v in ("True", "False"):
                    v = bool(v)
                else:
                    v = template.Variable(v)

        return v

#https://github.com/alexei/django-template-extensions
@register.tag("?:")
@register.tag("iif")
def iif(parser, token):
    #{% ?: exp1 exp2 exp3 %}
    #{% ?: exp1 exp2 %}
    try:
        tag, exp1, exp2, exp3 = token.split_contents()
    except ValueError:
        try:
            tag, exp1, exp2 = token.split_contents()
            exp3 = None
        except ValueError:
            raise template.TemplateSyntaxError("%r tag requires two or three arguments" % token.contents.split()[0])

    return IifNode(exp1 = exp1, exp2 = exp2, exp3 = exp3) 
#=========================================================
@register.filter('validarDimensaoImagem')
def validarDimensaoImagem(imagem,width,height):
    img = ImageFile.Image.open(imagem)
    (w,h) = img.size
    if w == width and h == height:
        return True
    else:
        return False
#=========================================================
@register.filter('validarDimensaoMaximaImagem')
def validarDimensaoMaximaImagem(imagem,width,height):
    img = ImageFile.Image.open(imagem)
    (w,h) = img.size
    if w <= width and h <= height:
        return True
    else:
        return False
#=========================================================
@register.filter('validarTamanhoMaximoPermitidoArquivo')
def validarTamanhoMaximoPermitidoArquivo(arquivo,limit_em_byte):
    #file = request.FILES['path_foto']
    #print file.name           # Gives name
    #print file.content_type   # Gives Content type text/html etc
    #print file.size           # Gives file's size in byte
    #print file.read()         # Reads file
    #http://pt.calcuworld.com/calculadoras-para-empresas/calculadora-de-bytes/
    # 1MB   => 1048576 byte
    # 500KB => 512000 byte
    #print '================='
    #print arquivo.size
    #print '================='
    if arquivo.size > limit_em_byte:
        return False
    else:
        return True

#=========================================================
#https://wellfire.co/learn/python-image-enhancements/
@register.filter('redimensionarImagem')
def redimensionarImagem(imagem,width,height):
    img = ImageFile.Image.open(imagem)
    if not width and not height:
        nova=img.resize((img.size[0] / 2, img.size[1] / 2),ImageFile.Image.ANTIALIAS).save("imagem.png")
    elif width and height:
        nova=img.resize((width,height),ImageFile.Image.ANTIALIAS).save("imagem.png")

    return nova
#=========================================================
@register.filter('cap')
def cap(value):
    namelist = value.split(' ')
    fixed = ''
    for name in namelist:
        name = name.lower()
        # fixes mcdunnough
        if name.startswith('mc'):
            sub = name.split('mc')
            name = "Mc" + sub[1].capitalize()
        # fixes "o'neill"
        elif name.startswith('o\''): 
            sub = name.split('o\'')
            name = "O'" + sub[1].capitalize()

        else: name = name.capitalize()
        
        nlist = name.split('-')
        for n in nlist:
            if len(n) > 1:
                up = n[0].upper()
                old = "-%s" % (n[0],)
                new = "-%s" % (up,)
                name = name.replace(old,new)

        fixed = fixed + " " + name
    return fixed
#=========================================================
@register.tag(name="switch")
def do_switch(parser, token):
    """
    The ``{% switch %}`` tag compares a variable against one or more values in
    ``{% case %}`` tags, and outputs the contents of the matching block.  An
    optional ``{% else %}`` tag sets off the default output if no matches
    could be found::

        {% switch result_count %}
            {% case 0 %}
                There are no search results.
            {% case 1 %}
                There is one search result.
            {% else %}
                Jackpot! Your search found {{ result_count }} results.
        {% endswitch %}

    Each ``{% case %}`` tag can take multiple values to compare the variable
    against::

        {% switch username %}
            {% case "Jim" "Bob" "Joe" %}
                Me old mate {{ username }}! How ya doin?
            {% else %}
                Hello {{ username }}
        {% endswitch %}
    """
    bits = token.contents.split()
    tag_name = bits[0]
    if len(bits) != 2:
        raise template.TemplateSyntaxError("'%s' tag requires one argument" % tag_name)
    variable = parser.compile_filter(bits[1])

    class BlockTagList(object):
        # This is a bit of a hack, as it embeds knowledge of the behaviour
        # of Parser.parse() relating to the "parse_until" argument.
        def __init__(self, *names):
            self.names = set(names)
        def __contains__(self, token_contents):
            name = token_contents.split()[0]
            return name in self.names

    # Skip over everything before the first {% case %} tag
    parser.parse(BlockTagList('case', 'endswitch'))

    cases = []
    token = parser.next_token()
    got_case = False
    got_else = False
    while token.contents != 'endswitch':
        nodelist = parser.parse(BlockTagList('case', 'else', 'endswitch'))

        if got_else:
            raise template.TemplateSyntaxError("'else' must be last tag in '%s'." % tag_name)

        contents = token.contents.split()
        token_name, token_args = contents[0], contents[1:]

        if token_name == 'case':
            tests = map(parser.compile_filter, token_args)
            case = (tests, nodelist)
            got_case = True
        else:
            # The {% else %} tag
            case = (None, nodelist)
            got_else = True
        cases.append(case)
        token = parser.next_token()

    if not got_case:
        raise template.TemplateSyntaxError("'%s' must have at least one 'case'." % tag_name)

    return SwitchNode(variable, cases)

class SwitchNode(Node):
    def __init__(self, variable, cases):
        self.variable = variable
        self.cases = cases

    def __repr__(self):
        return "<Switch node>"

    def __iter__(self):
        for tests, nodelist in self.cases:
            for node in nodelist:
                yield node

    def get_nodes_by_type(self, nodetype):
        nodes = []
        if isinstance(self, nodetype):
            nodes.append(self)
        for tests, nodelist in self.cases:
            nodes.extend(nodelist.get_nodes_by_type(nodetype))
        return nodes

    def render(self, context):
        try:
            value_missing = False
            value = self.variable.resolve(context, True)
        except VariableDoesNotExist:
            no_value = True
            value_missing = None

        for tests, nodelist in self.cases:
            if tests is None:
                return nodelist.render(context)
            elif not value_missing:
                for test in tests:
                    test_value = test.resolve(context, True)
                    if value == test_value:
                        return nodelist.render(context)
        else:
            return ""
#=========================================================
@register.simple_tag
def sort_table(request, field, value, direction=''):
    try:
        dict_ = request.GET.copy()
        if field == 'o' and field in dict_.keys():          
          if dict_[field].startswith('-') and dict_[field].lstrip('-') == value:
            dict_[field] = value
          elif dict_[field].lstrip('-') == value:
            dict_[field] = "-" + value
          else:
            dict_[field] = direction + value
        else:
          dict_[field] = direction + value
        
        return urlencode(OrderedDict(sorted(dict_.items())))
    except:
        pass        
#=========================================================
#http://stackoverflow.com/questions/1810891/django-how-to-filter-users-that-belong-to-a-specific-group
'''@register.simple_tag
def verificarGrupoUsuario(grupo_id, usuario_id):
    if grupo_id and usuario_id:
        retorno=Usuario.objects.filter(groups__id=grupo_id,id=usuario_id)
        #print retorno.query
        #print retorno
        if retorno:
            return True
    
    return False
'''    
#=========================================================
#http://wiki.python.org.br/VerificadorDeCPF
def validar_cpf(cpf,d1=0,d2=0,i=0):
    cpf= ''.join(re.findall("\d", cpf))
    
    if len(cpf)!=11:
        return False
    else:
        s=''.join(str(x) for x in cpf)
        if s=='00000000000' or s=='11111111111' or s=='22222222222' or s=='33333333333' or s=='44444444444' or s=='55555555555' or s=='66666666666' or s=='77777777777' or s=='88888888888' or s=='99999999999':
            return False

    while i<10:
        d1,d2,i=(d1+(int(cpf[i])*(11-i-1)))%11 if i<9 else d1,(d2+(int(cpf[i])*(11-i)))%11,i+1

    return (int(cpf[9])==(11-d1 if d1>1 else 0)) and (int(cpf[10])==(11-d2 if d2>1 else 0))
#=========================================================
def remover_mascara_numerica(value):
    return ''.join(re.findall("\d", value))
#=========================================================
def remover_mascara_alfanumerica(value):
    return ''.join(re.findall("\w", value))
#=========================================================
#https://docs.djangoproject.com/pt-br/1.10/topics/email/
#http://stackoverflow.com/questions/31324005/django-1-8-sending-mail-using-gmail-smtp
def send_email(para,assunto,mensagem):
    if para and assunto and mensagem:
        try:
            send_mail(assunto, mensagem,EMAIL_HOST_USER,[para])
        except Exception as e:
            print('%s%s' % ('Email não enviado=>',e))
    else:
        print('Preencha os campos corretamente para enviar um Email.')
#=========================================================
def verificar_campo_obrigatorio(campo,valor):
    if not valor:
        raise ValueError("O campo '%s' é obrigatório." % campo)
#=========================================================
