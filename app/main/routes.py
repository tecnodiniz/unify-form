import os
import uuid
from flask import Blueprint, flash, redirect, render_template, request, send_file, url_for, current_app
from werkzeug.utils import secure_filename
from app.services import (
    save_data,
    load_data, 
    allowed_file, 
    extract_questions,
    generate_unified_form,
    generate_xlsx_form,
    generate_html_form,
    generate_docx_form
    )

main_bp = Blueprint(
    "main",
    __name__)

@main_bp.route('/')
def index():
    data = load_data()
    return render_template('index.html', data=data)

@main_bp.route('/form/<form_id>')
def view_form(form_id):
    data = load_data()
    form = next((f for f in data["formularios"] if f["id"] == form_id), None)
    
    if not form:
        flash('Formulário não encontrado')
        return redirect(url_for('index'))
    
    return render_template('view_form.html', form=form)

@main_bp.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'files[]' not in request.files:
            flash('Nenhum arquivo selecionado')
            return redirect(request.url)
        
        files = request.files.getlist('files[]')
        product = request.form.get('produto', '')
        
        if not product:
            flash('Nome do produto é obrigatório')
            return redirect(request.url)
        
        if not files or files[0].filename == '':
            flash('Nenhum arquivo selecionado')
            return redirect(request.url)
        
        # Verificar se todos os arquivos são permitidos
        for file in files:
            if not allowed_file(file.filename):
                flash(f'Tipo de arquivo não permitido: {file.filename}')
                return redirect(request.url)
        
        # Processar arquivos
        all_questions = []
        insurers = []
        
   
        for file in files:
            filename = secure_filename(file.filename)
            insurer = request.form.get(f'seguradora_{files.index(file)}', 'Não especificada')
            insurers.append(insurer)
            
            file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], f"{uuid.uuid4()}_{filename}")
            file.save(file_path)
            
            # Extrair perguntas
          
            questions = extract_questions(file_path)
       
            all_questions.extend(questions)
        
        # Gerar formulário unificado
        
        unified_form = generate_unified_form(product, all_questions, insurers)
    
     
        
        # Gerar arquivos para download
        form_id = unified_form["id"]
        docx_path = os.path.join(current_app.config['FORMS_FOLDER'], f"{form_id}.docx")
        xlsx_path = os.path.join(current_app.config['FORMS_FOLDER'], f"{form_id}.xlsx")
        html_path = os.path.join(current_app.config['FORMS_FOLDER'], f"{form_id}.html")
        
        generate_docx_form(unified_form, docx_path)
        # generate_xlsx_form(unified_form, xlsx_path)
        generate_html_form(unified_form, html_path)
        
        # Adicionar produto à lista se não existir
        data = load_data()
        if product not in [p for p in data["produtos"]]:
            data["produtos"].append(product)
            save_data(data)
        
        return redirect(url_for('main.view_form', form_id=form_id))
    
    return render_template('upload.html')

@main_bp.route('/download/<form_id>/<format>')
def download_form(form_id, format):
    data = load_data()
    form = next((f for f in data["formularios"] if f["id"] == form_id), None)
    
    if not form:
        flash('Formulário não encontrado')
        return redirect(url_for('index'))
    
    if format == 'docx':
        file_path = os.path.join(current_app.config['FORMS_FOLDER'], f"{form_id}.docx")
        return send_file(file_path, as_attachment=True, download_name=f"formulario_{form['produto']}.docx")
    
    elif format == 'xlsx':
        file_path = os.path.join(current_app.config['FORMS_FOLDER'], f"{form_id}.xlsx")
        return send_file(file_path, as_attachment=True, download_name=f"formulario_{form['produto']}.xlsx")
    
    elif format == 'html':
        file_path = os.path.join(current_app.config['FORMS_FOLDER'], f"{form_id}.html")
        return send_file(file_path, as_attachment=True, download_name=f"formulario_{form['produto']}.html")
    
    else:
        flash('Formato não suportado')
        return redirect(url_for('main.view_form', form_id=form_id))

@main_bp.route('/online/<form_id>')
def online_form(form_id):
    data = load_data()
    form = next((f for f in data["formularios"] if f["id"] == form_id), None)
    
    if not form:
        flash('Formulário não encontrado')
        return redirect(url_for('index'))
    
    return render_template('online_form.html', form=form)

