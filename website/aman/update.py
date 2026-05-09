import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Unsplash images with Pexels
unsplash_to_pexels = {
    # hero
    'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=1920&q=80': 'https://images.pexels.com/photos/1571460/pexels-photo-1571460.jpeg?auto=compress&cs=tinysrgb&w=1920',
    'https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=1920&q=80': 'https://images.pexels.com/photos/323780/pexels-photo-323780.jpeg?auto=compress&cs=tinysrgb&w=1920',
    'https://images.unsplash.com/photo-1618221195710-dd6b41faaea6?w=1920&q=80': 'https://images.pexels.com/photos/276514/pexels-photo-276514.jpeg?auto=compress&cs=tinysrgb&w=1920',
    'https://images.unsplash.com/photo-1616486338812-3dadae4b4ace?w=1920&q=80': 'https://images.pexels.com/photos/1080721/pexels-photo-1080721.jpeg?auto=compress&cs=tinysrgb&w=1920',
    'https://images.unsplash.com/photo-1631679706909-1844bbd07221?w=1920&q=80': 'https://images.pexels.com/photos/262048/pexels-photo-262048.jpeg?auto=compress&cs=tinysrgb&w=1920',
    
    # about
    'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=800&q=80': 'https://images.pexels.com/photos/1571463/pexels-photo-1571463.jpeg?auto=compress&cs=tinysrgb&w=800',

    # services
    'https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=800&q=80': 'https://images.pexels.com/photos/323772/pexels-photo-323772.jpeg?auto=compress&cs=tinysrgb&w=800',
    'https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?w=800&q=80': 'https://images.pexels.com/photos/1080721/pexels-photo-1080721.jpeg?auto=compress&cs=tinysrgb&w=800',
    'https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?w=800&q=80': 'https://images.pexels.com/photos/1910472/pexels-photo-1910472.jpeg?auto=compress&cs=tinysrgb&w=800',
    'https://images.unsplash.com/photo-1598550476439-6847785fcea6?w=800&q=80': 'https://images.pexels.com/photos/3165335/pexels-photo-3165335.jpeg?auto=compress&cs=tinysrgb&w=800',
    'https://images.unsplash.com/photo-1593784991095-a205069470b6?w=800&q=80': 'https://images.pexels.com/photos/33129/popcorn-movie-party-entertainment.jpg?auto=compress&cs=tinysrgb&w=800',
    'https://images.unsplash.com/photo-1616594039964-ae9021a400a0?w=800&q=80': 'https://images.pexels.com/photos/262048/pexels-photo-262048.jpeg?auto=compress&cs=tinysrgb&w=800',
    'https://images.unsplash.com/photo-1497366216548-37526070297c?w=800&q=80': 'https://images.pexels.com/photos/380769/pexels-photo-380769.jpeg?auto=compress&cs=tinysrgb&w=800',

    # portfolio kitchen
    'https://images.unsplash.com/photo-1556909172-54557c7e4fb7?w=800&q=80': 'https://images.pexels.com/photos/2724749/pexels-photo-2724749.jpeg?auto=compress&cs=tinysrgb&w=800',
    'https://images.unsplash.com/photo-1600585152220-90363fe7e115?w=800&q=80': 'https://images.pexels.com/photos/2062426/pexels-photo-2062426.jpeg?auto=compress&cs=tinysrgb&w=800',
    
    # portfolio bedroom
    'https://images.unsplash.com/photo-1631049307264-da0ec9d70304?w=800&q=80': 'https://images.pexels.com/photos/1743227/pexels-photo-1743227.jpeg?auto=compress&cs=tinysrgb&w=800',

    # portfolio bathroom
    'https://images.unsplash.com/photo-1552321554-5fefe8c9ef14?w=800&q=80': 'https://images.pexels.com/photos/105934/pexels-photo-105934.jpeg?auto=compress&cs=tinysrgb&w=800',
    'https://images.unsplash.com/photo-1604709177225-055f99402ea3?w=800&q=80': 'https://images.pexels.com/photos/3288104/pexels-photo-3288104.jpeg?auto=compress&cs=tinysrgb&w=800',

    # portfolio gaming
    'https://images.unsplash.com/photo-1616588589676-62b3d4ff6643?w=800&q=80': 'https://images.pexels.com/photos/735911/pexels-photo-735911.jpeg?auto=compress&cs=tinysrgb&w=800',
    'https://images.unsplash.com/photo-1612287230202-1ff1d85d1bdf?w=800&q=80': 'https://images.pexels.com/photos/442576/pexels-photo-442576.jpeg?auto=compress&cs=tinysrgb&w=800',

    # portfolio theatre
    'https://images.unsplash.com/photo-1536440136628-849c177e76a1?w=800&q=80': 'https://images.pexels.com/photos/7991579/pexels-photo-7991579.jpeg?auto=compress&cs=tinysrgb&w=800',
    'https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?w=800&q=80': 'https://images.pexels.com/photos/109669/pexels-photo-109669.jpeg?auto=compress&cs=tinysrgb&w=800',

    # portfolio living
    'https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?w=800&q=80': 'https://images.pexels.com/photos/276528/pexels-photo-276528.jpeg?auto=compress&cs=tinysrgb&w=800',
    
    # 3d showcase
    'https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=600&q=80': 'https://images.pexels.com/photos/323780/pexels-photo-323780.jpeg?auto=compress&cs=tinysrgb&w=600',
    'https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?w=600&q=80': 'https://images.pexels.com/photos/1080721/pexels-photo-1080721.jpeg?auto=compress&cs=tinysrgb&w=600',
    'https://images.unsplash.com/photo-1618221195710-dd6b41faaea6?w=600&q=80': 'https://images.pexels.com/photos/262048/pexels-photo-262048.jpeg?auto=compress&cs=tinysrgb&w=600',
    'https://images.unsplash.com/photo-1598550476439-6847785fcea6?w=600&q=80': 'https://images.pexels.com/photos/3165335/pexels-photo-3165335.jpeg?auto=compress&cs=tinysrgb&w=600',
    'https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?w=600&q=80': 'https://images.pexels.com/photos/1910472/pexels-photo-1910472.jpeg?auto=compress&cs=tinysrgb&w=600',
    'https://images.unsplash.com/photo-1536440136628-849c177e76a1?w=600&q=80': 'https://images.pexels.com/photos/7991579/pexels-photo-7991579.jpeg?auto=compress&cs=tinysrgb&w=600',
    'https://images.unsplash.com/photo-1616486338812-3dadae4b4ace?w=600&q=80': 'https://images.pexels.com/photos/1571460/pexels-photo-1571460.jpeg?auto=compress&cs=tinysrgb&w=600',
    'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=600&q=80': 'https://images.pexels.com/photos/323772/pexels-photo-323772.jpeg?auto=compress&cs=tinysrgb&w=600'
}

for u, p in unsplash_to_pexels.items():
    content = content.replace(u, p)

# Now, add openPortfolioFilter logic to script
js_logic = '''
        // ============ PORTFOLIO FILTER ============
        function openPortfolioFilter(category) {
            const portfolioSection = document.getElementById('portfolio');
            if (portfolioSection) {
                portfolioSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
            const filterBtn = document.querySelector(`.filter-btn[data-filter="${category}"]`);
            if (filterBtn) {
                setTimeout(() => filterBtn.click(), 300);
            }
        }

        const filterBtns = document.querySelectorAll('.filter-btn');
'''

content = content.replace(
    '// ============ PORTFOLIO FILTER ============\n        const filterBtns = document.querySelectorAll(\'.filter-btn\');',
    js_logic
)

# Update the service card HTML
def replace_card(match):
    prefix = match.group(1)
    a_class = match.group(2)
    middle = match.group(3)
    title = match.group(4)
    
    cat = 'all'
    if 'Interior' in title: cat = 'living'
    elif 'Kitchen' in title: cat = 'kitchen'
    elif 'Bathroom' in title: cat = 'bathroom'
    elif 'Gaming' in title: cat = 'gaming'
    elif 'Theatre' in title: cat = 'theatre'
    elif 'Bedroom' in title: cat = 'bedroom'
    
    return f'<a href="javascript:void(0)" onclick="openPortfolioFilter(\'{cat}\')"{a_class}>{middle}<h3>{title}</h3>'

content = re.sub(
    r'(<a href="#contact"([^>]*)>)(.*?)(<h3>(.*?)</h3>)',
    replace_card,
    content,
    flags=re.DOTALL
)

# Update Instagram in footer
content = content.replace(
    '<a href="#" aria-label="Instagram"><i class="fab fa-instagram"></i></a>',
    '<a href="https://instagram.com/11__maverick_raptor" target="_blank" aria-label="Instagram"><i class="fab fa-instagram"></i></a>'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
