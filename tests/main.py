"""
MEDIA TYPE REPO TEST
async def get_all(mt: MediaTypeRepositories):
    media_types: List[MediaType] = await mt.get_all_media_type()

    for m in media_types:
        print(f'id: {m.id} name: {m.name}')


async def get_id(mt: MediaTypeRepositories, num):
    media_type: MediaType = await mt.get_media_type_id(num)

    print(f'id: {media_type.id} name: {media_type.name}')


async def add_mt(mt: MediaTypeRepositories, media: MediaType):
    await mt.add_media_type(media)


async def up_mt(mt: MediaTypeRepositories, media: MediaType):
    await mt.update_media_type(media)


async def get_mt_tr(mt: MediaTypeRepositories, t_id: int):
    media_type: MediaType = await mt.get_media_type_from_track(t_id)

    print(f'id: {media_type.id} name: {media_type.name}')


async def del_mt(mt: MediaTypeRepositories, num: int):
    await mt.delete_media_type(num)
"""

""" 
GENRE REPO TEST
async def get_all_genre(gnr: GenreRepositories):
    genres: List[Genre] = await gnr.get_all_genres()

    for genre in genres:
        print(f'id: {genre.id} name: {genre.name}')


async def get_id_genre(gnr: GenreRepositories, num):
    genre: Genre = await gnr.get_genres_id(num)

    print(f'id: {genre.id} name: {genre.name}')


async def add_genre(gnr: GenreRepositories, g: Genre):
    await gnr.add_genres(g)


async def delete_genre(gnr: GenreRepositories, id: int):
    await gnr.delete_genres(id)
"""
'''

async def get_all_artist(art: ArtistRepositories):
    artists: List[Artist] = await art.get_all_artist()

    for artist in artists:
        print(f'id: {artist.id} name: {artist.name}')
        for album in artist.albums:
            print(f'albums: {album}')
            for track in album.tracks:
                print(f'tracks:{track}')


async def get_id_artist(art: ArtistRepositories, num):
    artist: Artist = await art.get_artist_id(num)

    print(f'id: {artist.id} name: {artist.name}')
    print(f'Albums')
    for album in artist.albums:
        print(f'{album}')
        print('tracks:')
        for track in album.tracks:
            print(f'{track} \n')


async def add_artist(art: ArtistRepositories, artist: Artist):
    await art.add_artist(artist)


async def update_artist(art: ArtistRepositories, artist: Artist):
    await art.update_artist(artist)


async def delete_artist(art: ArtistRepositories, num: int):
    await art.delete_artist(num)
'''

"""
ALBUM REPO TEST

async def get_all_album(album_repo: AlbumRepositories) -> None:
    albums: List[Album] = await album_repo.get_all_album()

    for album in albums:
        print(f'{album}')


async def get_id_album(album_repo: AlbumRepositories, num):
    album: Album = await album_repo.get_album_id(num)
    print(f'{album}')


async def add_album(album_repo: AlbumRepositories, album: Album, num: int):
    await album_repo.add_album(
        album,
        num
    )

async def update_album(album_repo: AlbumRepositories, album: Album, num: int):
    await album_repo.update_album(album, num)


async def delete_album(album_repo: AlbumRepositories, num: int):
    await album_repo.delete_album(num)


"""

"""
TRACK REPO TEST 

async def get_all_tracks(t_repo: TrackRepository):
    tracks: List[Track] = await t_repo.get_all_tracks()
    for track in tracks:
        print(f'{track}')


async def get_id_track(t_repo: TrackRepository, num):
    track: Track = await t_repo.get_track_by_id(num)
    print(f'{track}')


async def get_albums_tracks(t_repo: TrackRepository, album_id: int):
    tracks: List[Track] = await t_repo.get_tracks_from_album(album_id)
    for track in tracks:
        print(f'{track}')


async def get_track_playlist(t_repo: TrackRepository, pl_id: int):
    tracks: List[Track] = await t_repo.get_tracks_from_playlist(pl_id)
    for track in tracks:
        print(f'{track}')


async def add_track(t_repo: TrackRepository, track: Track):
    await t_repo.add_track(
        track
    )


async def update_track(t_repo: TrackRepository, track: Track):
    await t_repo.update_track(track)


async def delete_track(t_repo: TrackRepository, id: int):
    await t_repo.delete_track(id)

"""

"""
Invoice ITEM REPO TEST


async def get_all_item(item_inv: InvoiceItemRepositories):
    invoice_items: List[InvoiceItems] = await item_inv.get_all_invoice_item()

    for item in invoice_items:
        print(f'{item}')


async def get_id_item(item_inv: InvoiceItemRepositories, num: int):
    invoice_item: InvoiceItems = await item_inv.get_invoice_item_by_id(num)
    print(f'{invoice_item}')


async def get_invoice_item(item_inv: InvoiceItemRepositories, num: int):
    invoice_items: List[InvoiceItems] = await item_inv.get_invoice_item_from_invoice_id(num)

    for item in invoice_items:
        print(f'{item}')


async def add_invoice_item(item_inv: InvoiceItemRepositories, invoice_item: InvoiceItems, invoice_id):
    await item_inv.add_invoice_item(invoice_item, invoice_id)

    invoice: InvoiceItems = await item_inv.get_invoice_item_by_id(invoice_item.id)
    print(f'{invoice}')


async def delete_invoice_item(item_inv: InvoiceItemRepositories, item_id: int):
    await item_inv.delete_invoice_item(item_id)


async def update_invoice_item(item_inv: InvoiceItemRepositories, invoice_item: InvoiceItems, invoice_id):
    await item_inv.get_invoice_item_by_id(invoice_item.id)
    print('')
    await item_inv.update_invoice_item(invoice_item, invoice_id)
    print('')
    await item_inv.get_invoice_item_by_id(invoice_item.id)

"""

"""
INVOICE REPO TEST 

async def get_all_invoices(invoice_repo: InvoiceRepositories):
    invoices: List[Invoice] = await invoice_repo.get_all_invoice()

    for invoice in invoices:
        print(f'{invoice}')


async def get_id_invoices(invoice_repo: InvoiceRepositories, num: int):
    invoice: Invoice = await invoice_repo.get_invoice_by_id(num)
    print(f'{invoice}')


async def get_customer_invoices(invoice_repo: InvoiceRepositories, num: int):
    invoices: List[Invoice] = await invoice_repo.get_invoice_by_customer_id(num)

    for invoice in invoices:
        print(f'{invoice}')


async def add_invoice(invoice_repo: InvoiceRepositories, invoice: Invoice, customer_id: int):
    await invoice_repo.add_invoice(invoice, customer_id)
    await get_id_invoices(invoice_repo, invoice.id)


async def update_invoice(invoice_repo: InvoiceRepositories, invoice: Invoice, customer_id: int):
    await get_id_invoices(invoice_repo, invoice.id)
    await invoice_repo.update_invoice(invoice, customer_id)
    print(f'NEW')
    await get_id_invoices(invoice_repo, invoice.id)


async def delete_invoice(invoice_repo: InvoiceRepositories, id: int):
    await invoice_repo.delete_invoice(id)


async def add_test_invoice():
    try:
        inv = await invoice_item_repo.get_invoice_item_by_id(34000)
    except ValueError as e:
        inv = None

    if inv:
        await invoice_item_repo.delete_invoice_item(34000)
        await invoice_item_repo.delete_invoice_item(34001)

    track1, track2, *_ = await track_repo.get_all_tracks()

    invoices_items = [InvoiceItems(34000, track2, 15000, 1),
                      InvoiceItems(34001, track2, 15000, 1)]

    invoice = Invoice(
        id=3000,
        date=datetime.now(),
        address='ddd',
        city='capital',
        state='cba',
        country='argentina',
        postalcode=5000,
        price_total=0,
        items=invoices_items
    )

    await add_invoice(invoice_repo, invoice, 1)


async def test_update():
    track1, track2, *_ = await track_repo.get_all_tracks()

    invoices_items = [InvoiceItems(34000, track2, 15000, 1),
                      InvoiceItems(34001, track2, 15000, 1)]

    invoice = Invoice(
        id=3000,
        date=datetime.now(),
        address='alberdi',
        city='capital',
        state='cba',
        country='argentina',
        postalcode=5000,
        price_total=0,
        items=invoices_items
    )

    await update_invoice(invoice_repo, invoice, 2)

async def test_delete():

    await invoice_repo.delete_invoice(3000)
    await invoice_item_repo.delete_invoice_item(34000)
    await invoice_item_repo.delete_invoice_item(34001)
"""

"""
CUSTOMER TEST REPO 

async def get_all_customer(custom_repo: CustomerRepositories):
    customers: List[Customer] = await custom_repo.get_all_customers()

    for customer in customers:
        print(f'{customer}')


async def get_id_customer(custom_repo: CustomerRepositories, id: int):
    customer = await custom_repo.get_customers_by_id(id)

    print(f'{customer}')


async def get_customer_employed(custom_repo: CustomerRepositories, employed_id: int):
    customers: List[Customer] = await custom_repo.get_customers_by_employed(employed_id)

    for customer in customers:
        print(f'{customer}')


async def add_customer(custom_repo: CustomerRepositories, customer: Customer, employed_id: int):
    await custom_repo.add_customers(customer, employed_id)


async def update_customer(custom_repo: CustomerRepositories, customer: Customer, employed_id: int):
    await custom_repo.update_customers(customer, employed_id)


async def test_add_customer():
    employed_id: int = 3

    customer = Customer(
        30000,
        'Francisco',
        'Begliardo',
        'UTN FRC',
        'Av colon',
        'Capital',
        'Cordoba',
        'Argentina',
        '5000',
        '3472629461',
        'fax',
        'panchobegliardo@gmail.com',
        []
    )

    await add_customer(customer_repo, customer, employed_id)


async def test_update_customer():
    employed_id: int = 4

    customer = Customer(
        30000,
        'Francisco Hugo',
        'Begliardo',
        'UTN FRC',
        'Av colon',
        'Capital',
        'Cordoba',
        'Argentina',
        '5000',
        '3472629461',
        'fax',
        'panchobegliardo@gmail.com',
        []
    )

    await update_customer(customer_repo, customer, employed_id)

"""

""""
EMPLOTED TEST REPO 
async def get_all_employed(employed_repo: EmployedRepositoryImpl):
    employees: List[Employed] = await employed_repo.get_all_employed()

    for employe in employees:
        print(f'{employe}')


async def get_id_employed(employed_repo: EmployedRepositoryImpl, id: int):
    employed: Employed = await employed_repo.get_employed_by_id(id)

    print(f'{employed}')


async def add_employed(employed_repo: EmployedRepositoryImpl, employed: Employed):
    await employed_repo.add_employed(employed)

    await employed_repo.get_employed_by_id(employed.id)


async def update_employed(employed_repo: EmployedRepositoryImpl, employed: Employed):
    await employed_repo.update_employed(employed)


async def delete_employed(employed_repo: EmployedRepositoryImpl, id: int):
    await employed_repo.delete_employed(id)


async def test_AGU(employed_repo: EmployedRepositoryImpl, employed: Employed):
    await employed_repo.delete_employed(employed.id)
    print('GET ALL \n')
    await employed_repo.get_all_employed()
    print('ADD\n')
    await employed_repo.add_employed(employed)
    print('GET ID')
    await employed_repo.get_employed_by_id(employed.id)
    print('UPDATE')
    employed.firstName = 'Francisco'
    employed.lastName = 'Begliardo'
    await employed_repo.update_employed(employed)
    print('GET ID')
    await employed_repo.get_employed_by_id(employed.id)


empl = Employed(
             id=9,
             last_name='francisco',
             first_name='begliardo',
             title='',
             birthdate=datetime.now(),
             hiredate=datetime.now(),
             address='Av colon 1420',
             city='Capital',
             state='CBA',
             country='Argentina',
             postalcode='5000',
             phone='3472629461',
             fax='',
             email='panchobegliardo@gmail.com',
             reports_to=None,
             customer=None
)
"""