function HatsList(props) {
    const DeleteHat = async(id) => {
        const deleteUrl = `http://localhost:8090/api/hats/${id}/`
        const fetchConfig = {
            method: "delete"
        }
        const response = await fetch(deleteUrl, fetchConfig);
        if (response.ok) {
            window.location.reload();
        }
    }

  return (
    <table className="table table-striped">
      <thead>
        <tr>
          <th>Image</th>
          <th>Name</th>
          <th>Fabric</th>
          <th>Style</th>
          <th>Color</th>
          <th>Closet Name</th>
          <th>Section Number</th>
          <th>Shelf Number</th>
        </tr>
      </thead>
      <tbody>
        {props.hats.map(hat => {
          return (
            <tr key={hat.id}>
              <td>
                <img src={hat.picture_url} height="100" width="100" />
              </td>
              <td>{hat.name}</td>
              <td>{hat.fabric}</td>
              <td>{hat.style}</td>
              <td>{hat.color}</td>
              <td>{hat.location.closet_name}</td>
              <td>{hat.location.section_number}</td>
              <td>{hat.location.shelf_number}</td>
              <button className="btn btn-primary" onClick={() => DeleteHat(hat.id)}>
                Delete
              </button>
            </tr>
          );
        })}
      </tbody>
    </table>
  );
}

export default HatsList;